package com.example.blackburnweighttracker;

import androidx.appcompat.app.AppCompatActivity;

import android.Manifest;
import android.content.Intent;                     //New: for Notifications button
import android.content.pm.PackageManager;
import android.telephony.SmsManager;
import android.util.Log;
import androidx.core.content.ContextCompat;

import android.content.SharedPreferences;
import android.database.Cursor;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TableLayout;
import android.widget.TableRow;
import android.widget.TextView;
import android.widget.Toast;

import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;

public class DashboardActivity extends AppCompatActivity {

    private TextView textCurrentDate;                           //Constructors
    private TextView textCurrentWeight;
    private Button buttonDecreaseWeight;
    private Button buttonIncreaseWeight;
    private Button buttonSaveWeight;
    private TableLayout tableRecentEntries;

    private Button buttonChangeDate;                            //Notifications button

    private WeightTrackerDbHelper dbHelper;
    private int currentUserId;
    private int currentWeight = 170;

    private static final String DATE_FORMAT = "MM-dd-yyyy";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);

        dbHelper = new WeightTrackerDbHelper(this);                                     //Database and User Setup

        SharedPreferences prefs = getSharedPreferences(MainActivity.PREFS_NAME, MODE_PRIVATE);
        currentUserId = prefs.getInt(MainActivity.KEY_USER_ID, -1);
        if (currentUserId == -1) {                                                      //If no user, send back to login
            finish();
            return;
        }

        textCurrentDate = findViewById(R.id.textCurrentDate);                           //View Bindings
        textCurrentWeight = findViewById(R.id.textCurrentWeight);
        buttonDecreaseWeight = findViewById(R.id.buttonDecreaseWeight);
        buttonIncreaseWeight = findViewById(R.id.buttonIncreaseWeight);
        buttonSaveWeight = findViewById(R.id.buttonSaveWeight);
        tableRecentEntries = findViewById(R.id.tableRecentEntries);
        buttonChangeDate = findViewById(R.id.buttonChangeDate);                        //Notifications button binding

        String today = new SimpleDateFormat(DATE_FORMAT, Locale.getDefault()).format(new Date());
        textCurrentDate.setText(today);

        textCurrentWeight.setText(String.valueOf(currentWeight));

        buttonDecreaseWeight.setOnClickListener(new View.OnClickListener() {           //Weight Decreaser
            @Override
            public void onClick(View v) {
                currentWeight--;
                textCurrentWeight.setText(String.valueOf(currentWeight));
            }
        });

        buttonIncreaseWeight.setOnClickListener(new View.OnClickListener() {           //Weight Increaser
            @Override
            public void onClick(View v) {
                currentWeight++;
                textCurrentWeight.setText(String.valueOf(currentWeight));
            }
        });

        buttonSaveWeight.setOnClickListener(new View.OnClickListener() {               //Weight Saver
            @Override
            public void onClick(View v) {
                saveWeightEntry();
            }
        });

        buttonChangeDate.setOnClickListener(new View.OnClickListener() {               //Notifications Page
            @Override
            public void onClick(View v) {
                Intent intent = new Intent(DashboardActivity.this, NotificationActivity.class);
                startActivity(intent);
            }
        });

        populateRecentEntries();
    }

    private void saveWeightEntry() {                                                   //Save helper
        String date = textCurrentDate.getText().toString();
        double weightValue = Double.parseDouble(textCurrentWeight.getText().toString());

        long result = dbHelper.addWeightEntry(currentUserId, date, weightValue);       //New: Insert only method

        if (result == -1) {
            Toast.makeText(this, "Error, try again.", Toast.LENGTH_SHORT).show();
        } else {
            Toast.makeText(this, "Saved successful.", Toast.LENGTH_SHORT).show();
            populateRecentEntries();                                                   // refresh grid

            checkGoalAndSendSms(weightValue);
        }
    }

    private void populateRecentEntries() {                                             //Clear existing rows, saving header (index 0)
        int childCount = tableRecentEntries.getChildCount();
        if (childCount > 1) {
            tableRecentEntries.removeViews(1, childCount - 1);
        }

        Cursor cursor = dbHelper.getWeightsForUser(currentUserId);                    //Get all entries for current user, use helper
        if (cursor != null) {
            while (cursor.moveToNext()) {                                             //Adjust column names
                final int weightId = cursor.getInt(
                        cursor.getColumnIndexOrThrow(WeightTrackerDbHelper.COLUMN_WEIGHT_ID));
                String date = cursor.getString(
                        cursor.getColumnIndexOrThrow(WeightTrackerDbHelper.COLUMN_ENTRY_DATE));
                double weightValue = cursor.getDouble(
                        cursor.getColumnIndexOrThrow(WeightTrackerDbHelper.COLUMN_WEIGHT_VALUE));

                TableRow row = new TableRow(this);

                TextView dateView = new TextView(this);                               //Date column
                dateView.setText(date);
                dateView.setPadding(16, 8, 32, 8);

                TextView weightView = new TextView(this);                             //Weight column
                weightView.setText(String.format(Locale.getDefault(), "%.1f", weightValue));
                weightView.setPadding(16, 8, 32, 8);

                TextView progressView = new TextView(this);                           //Progress column
                progressView.setPadding(16, 8, 32, 8);

                double goalWeight = 150.0;
                double diff = weightValue - goalWeight;
                String progressText;
                if (diff > 0) {
                    progressText = String.format(Locale.getDefault(), "+%.1f lbs", diff);
                } else if (diff < 0) {
                    progressText = String.format(Locale.getDefault(), "%.1f lbs", diff); // negative
                } else {
                    progressText = "At goal";
                }
                progressView.setText(progressText);

                Button deleteButton = new Button(this);                               //Delete button
                deleteButton.setText("X");
                deleteButton.setAllCaps(false);
                deleteButton.setBackgroundTintList(
                        ContextCompat.getColorStateList(this, R.color.wt_primary_light));
                deleteButton.setTextColor(
                        ContextCompat.getColor(this, R.color.wt_primary_dark));
                deleteButton.setOnClickListener(new View.OnClickListener() {
                    @Override
                    public void onClick(View v) {
                        dbHelper.deleteWeight(weightId);
                        populateRecentEntries();
                        Toast.makeText(DashboardActivity.this,
                                "Entry deleted.", Toast.LENGTH_SHORT).show();
                    }
                });

                // Add views to row
                row.addView(dateView);
                row.addView(weightView);
                row.addView(progressView);
                row.addView(deleteButton);

                // Add row to table
                tableRecentEntries.addView(row);
            }
            cursor.close();
        }
    }

    private void checkGoalAndSendSms(double latestWeight) {                            //SMS handling for Goals
        Log.d("WeightTracker", "checkGoalAndSendSms called. latestWeight=" + latestWeight);     //sanity checker for debugging; comment out
        SharedPreferences prefs = getSharedPreferences(MainActivity.PREFS_NAME, MODE_PRIVATE);
        boolean smsEnabled = prefs.getBoolean("sms_enabled", false);
        boolean smsGoal = prefs.getBoolean("sms_goal", true);

        if (!smsEnabled || !smsGoal) {                                                //Check if user has disabled SMS or alerts.
            return;
        }

        double goalWeight = 150.0;                                                    //Goal Default Value

        if (latestWeight <= goalWeight) {                                             //Check if goal needs to be reached still

            int permissionCheck = ContextCompat.checkSelfPermission(
                    this, Manifest.permission.SEND_SMS);

            if (permissionCheck != PackageManager.PERMISSION_GRANTED) {               //Permission is not granted.
                Log.d("WeightTracker", "SMS permission not granted, no SMS will be sent.");
                return;
            }

            String phoneNumber = "5554";                                              //Test phone number for emulator
            String message = "You did it! You've reached your goal weight of " + goalWeight + " lbs.";

            try {
                SmsManager smsManager = SmsManager.getDefault();
                smsManager.sendTextMessage(phoneNumber, null, message, null, null);
                Log.d("WeightTracker", "Goal SMS sent: " + message);
            } catch (Exception e) {
                Log.e("WeightTracker", "Error sending SMS: " + e.getMessage());
            }
        }
    }
}
