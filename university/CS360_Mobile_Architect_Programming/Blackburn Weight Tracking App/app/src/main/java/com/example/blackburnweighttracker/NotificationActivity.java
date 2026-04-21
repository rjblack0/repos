package com.example.blackburnweighttracker;

import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.app.ActivityCompat;
import androidx.core.content.ContextCompat;

import android.Manifest;
import android.content.SharedPreferences;
import android.content.pm.PackageManager;
import android.os.Bundle;
import android.view.View;
import android.widget.CheckBox;
import android.widget.Switch;
import android.widget.TextView;

public class NotificationActivity extends AppCompatActivity {           //Notification activity

    private static final int REQUEST_SMS_PERMISSION = 1001;

    private Switch switchEnableSms;
    private CheckBox checkGoalReached;
    private CheckBox checkWeeklySummary;
    private TextView textPermissionStatus;

    @Override
    protected void onCreate(Bundle savedInstanceState) {                //New
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_notification);

        switchEnableSms = findViewById(R.id.switchEnableSms);
        checkGoalReached = findViewById(R.id.checkGoalReached);
        checkWeeklySummary = findViewById(R.id.checkWeeklySummary);
        textPermissionStatus = findViewById(R.id.textPermissionStatus);

        loadPreferences();
        updatePermissionStatusText();

        switchEnableSms.setOnCheckedChangeListener((buttonView, isChecked) -> savePreferences());
        checkGoalReached.setOnCheckedChangeListener((buttonView, isChecked) -> savePreferences());
        checkWeeklySummary.setOnCheckedChangeListener((buttonView, isChecked) -> savePreferences());
    }

    private void loadPreferences() {                                                                //Loader
        SharedPreferences prefs = getSharedPreferences(MainActivity.PREFS_NAME, MODE_PRIVATE);
        boolean enabled = prefs.getBoolean("sms_enabled", false);
        boolean goal = prefs.getBoolean("sms_goal", true);
        boolean weekly = prefs.getBoolean("sms_weekly", false);

        switchEnableSms.setChecked(enabled);
        checkGoalReached.setChecked(goal);
        checkWeeklySummary.setChecked(weekly);
    }

    private void savePreferences() {                                                                //Saver, preferences
        SharedPreferences prefs = getSharedPreferences(MainActivity.PREFS_NAME, MODE_PRIVATE);
        prefs.edit()
                .putBoolean("sms_enabled", switchEnableSms.isChecked())
                .putBoolean("sms_goal", checkGoalReached.isChecked())
                .putBoolean("sms_weekly", checkWeeklySummary.isChecked())
                .apply();
    }

    private void updatePermissionStatusText() {                                                     //Updater, displays message
        int permissionCheck = ContextCompat.checkSelfPermission(
                this, Manifest.permission.SEND_SMS);

        if (permissionCheck == PackageManager.PERMISSION_GRANTED) {
            textPermissionStatus.setText("SMS permission is granted.");
        } else {
            textPermissionStatus.setText("SMS permission is denied.");
        }
    }

    public void onRequestSmsPermissionClicked(View view) {                      //Button caller, use onClick in XML
        int permissionCheck = ContextCompat.checkSelfPermission(
                this, Manifest.permission.SEND_SMS);

        if (permissionCheck == PackageManager.PERMISSION_GRANTED) {
            updatePermissionStatusText();
        } else {
            ActivityCompat.requestPermissions(
                    this,
                    new String[]{Manifest.permission.SEND_SMS},
                    REQUEST_SMS_PERMISSION
            );
        }
    }

    @Override
    public void onRequestPermissionsResult(int requestCode,                         //Add overrider
                                           @NonNull String[] permissions,
                                           @NonNull int[] grantResults) {
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);

        if (requestCode == REQUEST_SMS_PERMISSION) {
            if (grantResults.length > 0 &&
                    grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                updatePermissionStatusText();
            } else {
                updatePermissionStatusText();
            }
        }
    }
}
