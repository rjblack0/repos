package com.example.blackburnweighttracker;

import android.content.Context;
import android.database.sqlite.SQLiteDatabase;
import android.database.sqlite.SQLiteOpenHelper;
import android.content.ContentValues;
import android.database.Cursor;

public class WeightTrackerDbHelper extends SQLiteOpenHelper {

    private static final String DATABASE_NAME = "weight_tracker.db";
    private static final int DATABASE_VERSION = 1;

    public static final String TABLE_USERS = "users";                       //User table
    public static final String COLUMN_USER_ID = "id";
    public static final String COLUMN_USERNAME = "username";
    public static final String COLUMN_PASSWORD = "password";

    public static final String TABLE_WEIGHTS = "weights";                   //Weights table
    public static final String COLUMN_WEIGHT_ID = "id";
    public static final String COLUMN_WEIGHT_USER_ID = "user_id";
    public static final String COLUMN_ENTRY_DATE = "entry_date";
    public static final String COLUMN_WEIGHT_VALUE = "weight_value";
    public static final String COLUMN_NOTE = "note";

    public WeightTrackerDbHelper(Context context) {
        super(context, DATABASE_NAME, null, DATABASE_VERSION);
    }

    @Override
    public void onCreate(SQLiteDatabase db) {
        String createUsers = "CREATE TABLE " + TABLE_USERS + " ("
                + COLUMN_USER_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, "
                + COLUMN_USERNAME + " TEXT UNIQUE NOT NULL, "
                + COLUMN_PASSWORD + " TEXT NOT NULL);";

        String createWeights = "CREATE TABLE " + TABLE_WEIGHTS + " ("
                + COLUMN_WEIGHT_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, "
                + COLUMN_WEIGHT_USER_ID + " INTEGER NOT NULL, "
                + COLUMN_ENTRY_DATE + " TEXT NOT NULL, "
                + COLUMN_WEIGHT_VALUE + " REAL NOT NULL, "
                + COLUMN_NOTE + " TEXT, "
                + "FOREIGN KEY(" + COLUMN_WEIGHT_USER_ID + ") REFERENCES "
                + TABLE_USERS + "(" + COLUMN_USER_ID + "));";

        db.execSQL(createUsers);
        db.execSQL(createWeights);
    }

    @Override
    public void onUpgrade(SQLiteDatabase db, int oldVersion, int newVersion) {
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_WEIGHTS);
        db.execSQL("DROP TABLE IF EXISTS " + TABLE_USERS);
        onCreate(db);
    }

    public long addUser(String username, String password) {                 //New user register
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues values = new ContentValues();
        values.put(COLUMN_USERNAME, username);
        values.put(COLUMN_PASSWORD, password);
        return db.insert(TABLE_USERS, null, values);
    }

    public int validateUser(String username, String password) {             //Return user ID, store
        SQLiteDatabase db = this.getReadableDatabase();
        String[] columns = { COLUMN_USER_ID };
        String selection = COLUMN_USERNAME + "=? AND " + COLUMN_PASSWORD + "=?";
        String[] selectionArgs = { username, password };

        Cursor cursor = db.query(TABLE_USERS, columns, selection,
                selectionArgs, null, null, null);

        int userId = -1;
        if (cursor != null) {
            if (cursor.moveToFirst()) {
                userId = cursor.getInt(cursor.getColumnIndexOrThrow(COLUMN_USER_ID));
            }
            cursor.close();
        }
        return userId;
    }

    public long addWeightEntry(int userId, String date, double weight) {    //New weight entry, always insert
        SQLiteDatabase db = this.getWritableDatabase();
        ContentValues values = new ContentValues();
        values.put(COLUMN_WEIGHT_USER_ID, userId);
        values.put(COLUMN_ENTRY_DATE, date);
        values.put(COLUMN_WEIGHT_VALUE, weight);
        return db.insert(TABLE_WEIGHTS, null, values);
    }

    public Cursor getWeightsForUser(int userId) {                           //Get weights for user
        SQLiteDatabase db = this.getReadableDatabase();
        String orderBy = COLUMN_ENTRY_DATE + " DESC";
        return db.query(TABLE_WEIGHTS, null,
                COLUMN_WEIGHT_USER_ID + "=?",
                new String[]{String.valueOf(userId)},
                null, null, orderBy);
    }

    public int deleteWeight(int weightId) {                                 //Entry deleter option
        SQLiteDatabase db = this.getWritableDatabase();
        return db.delete(TABLE_WEIGHTS, COLUMN_WEIGHT_ID + "=?",
                new String[]{String.valueOf(weightId)});
    }
}
