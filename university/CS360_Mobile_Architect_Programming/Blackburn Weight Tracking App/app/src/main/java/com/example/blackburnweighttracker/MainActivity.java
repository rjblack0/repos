package com.example.blackburnweighttracker;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.text.TextUtils;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    private EditText editTextUsername;
    private EditText editTextPassword;
    private Button buttonLogin;
    private Button buttonCreateAccount;

    private WeightTrackerDbHelper dbHelper;

    public static final String PREFS_NAME = "WeightTrackerPrefs";
    public static final String KEY_USER_ID = "currentUserId";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        dbHelper = new WeightTrackerDbHelper(this);

        editTextUsername = findViewById(R.id.editTextUsername);
        editTextPassword = findViewById(R.id.editTextPassword);
        buttonLogin = findViewById(R.id.buttonLogin);
        buttonCreateAccount = findViewById(R.id.buttonCreateAccount);

        //SharedPreferences prefs = getSharedPreferences(PREFS_NAME, MODE_PRIVATE);           //Skip login if user already logged in
        //int savedUserId = prefs.getInt(KEY_USER_ID, -1);                                      //Option disabled for testing login
        //if (savedUserId != -1) {
        //    navigateToDashboard();
        //}

        buttonLogin.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                handleLogin();
            }
        });

        buttonCreateAccount.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                handleCreateAccount();
            }
        });
    }

    private void handleLogin() {                                                    //Login Starter
        String username = editTextUsername.getText().toString().trim();
        String password = editTextPassword.getText().toString().trim();

        if (TextUtils.isEmpty(username) || TextUtils.isEmpty(password)) {
            Toast.makeText(this, "Please enter a username and password.", Toast.LENGTH_SHORT).show();
            return;
        }

        int userId = dbHelper.validateUser(username, password);                     //Success / fail option
        if (userId != -1) {
            saveCurrentUser(userId);
            Toast.makeText(this, "Login successful!", Toast.LENGTH_SHORT).show();
            navigateToDashboard();
        } else {
            Toast.makeText(this, "Invalid username / password.", Toast.LENGTH_SHORT).show();
        }
    }

    private void handleCreateAccount() {                                            //Create Account
        String username = editTextUsername.getText().toString().trim();
        String password = editTextPassword.getText().toString().trim();

        if (TextUtils.isEmpty(username) || TextUtils.isEmpty(password)) {
            Toast.makeText(this, "Please enter a username and password.", Toast.LENGTH_SHORT).show();
            return;
        }

        long rowId = dbHelper.addUser(username, password);                          //Success / Fail option
        if (rowId == -1) {
            Toast.makeText(this, "Error: Username already exists.", Toast.LENGTH_SHORT).show();
        } else {
            Toast.makeText(this, "Account created! You can now log in.", Toast.LENGTH_SHORT).show();

            int newUserId = (int) rowId;
            saveCurrentUser(newUserId);
            navigateToDashboard();
        }
    }

    private void saveCurrentUser(int userId) {                                      //Store user info
        SharedPreferences prefs = getSharedPreferences(PREFS_NAME, MODE_PRIVATE);
        prefs.edit().putInt(KEY_USER_ID, userId).apply();
    }

    private void navigateToDashboard() {                                            //Exit
        Intent intent = new Intent(MainActivity.this, DashboardActivity.class);
        startActivity(intent);
        finish();
    }
}
