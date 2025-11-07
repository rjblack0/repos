//### LAYOUTS  ###//

//LinearLayout → horizontal/vertical stacks

<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:orientation="vertical"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Button 1" />
</LinearLayout>

//RelativeLayout → position views relative to others/parent

<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent" android:layout_height="match_parent">

    <TextView
        android:id="@+id/label"
        android:layout_width="wrap_content" android:layout_height="wrap_content"
        android:layout_alignParentTop="true"
        android:text="Username:" />

    <EditText
        android:id="@+id/input"
        android:layout_width="wrap_content" android:layout_height="wrap_content"
        android:layout_toRightOf="@id/label"
        android:layout_alignBaseline="@id/label"/>
</RelativeLayout>

//ConstraintLayout → modern flexible layout (use for most screens)

<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent" android:layout_height="match_parent">

    <TextView
        android:id="@+id/tv"
        android:layout_width="wrap_content" android:layout_height="wrap_content"
        android:text="Text"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintStart_toStartOf="parent"/>

    <Button
        android:id="@+id/btn"
        android:layout_width="wrap_content" android:layout_height="wrap_content"
        android:text="Go"
        app:layout_constraintBaseline_toBaselineOf="@id/tv"
        app:layout_constraintStart_toEndOf="@id/tv"/>
</androidx.constraintlayout.widget.ConstraintLayout>

//TableLayout → simple forms in rows/columns

<TableLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent" android:layout_height="wrap_content">

    <TableRow>
        <TextView android:text="Username:"/>
        <EditText android:layout_width="0dp" android:layout_height="wrap_content"
                  android:layout_weight="1"/>
    </TableRow>
    <TableRow>
        <Button android:text="Login" android:layout_column="1"/>
    </TableRow>
</TableLayout>

//GridLayout → grid with specified columnCount

<GridLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent" android:layout_height="wrap_content"
    android:columnCount="2" android:useDefaultMargins="true">

    <TextView
        android:layout_columnSpan="2"
        android:layout_gravity="center_horizontal"
        android:text="Please login:"/>

    <TextView android:text="Username:"/>
    <EditText android:layout_gravity="fill_horizontal"/>

    <TextView android:text="Password:"/>
    <EditText android:inputType="textPassword"
              android:layout_gravity="fill_horizontal"/>

    <Button android:text="Login" android:layout_column="1"
            android:layout_gravity="right"/>
</GridLayout>

//FrameLayout → overlay views (stacking)

<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent" android:layout_height="200dp">

    <ImageView
        android:src="@mipmap/ic_launcher"
        android:layout_width="150dp" android:layout_height="150dp"
        android:layout_gravity="center"/>

    <TextView
        android:text="FrameLayout Example"
        android:layout_width="match_parent" android:layout_height="match_parent"
        android:gravity="center"/>
</FrameLayout>

//###WIDGETS AND EVENTS ###//

//Button / ImageButton → click actions
<Button
    android:id="@+id/btnGo"
    android:layout_width="wrap_content" android:layout_height="wrap_content"
    android:text="Go" android:onClick="onGoClicked"/>

<ImageButton
    android:id="@+id/btnHelp"
    android:layout_width="wrap_content" android:layout_height="wrap_content"
    android:src="@drawable/ic_help" android:contentDescription="@string/help"/>

public void onGoClicked(View v) { /* ... */ }

Button b = findViewById(R.id.btnGo);
b.setOnClickListener(v ->
    Toast.makeText(this, "Clicked", Toast.LENGTH_SHORT).show());


//FloatingActionButton (Material)

<com.google.android.material.floatingactionbutton.FloatingActionButton
    android:id="@+id/fabAdd"
    android:layout_width="wrap_content" android:layout_height="wrap_content"
    android:src="@drawable/ic_add" android:onClick="onAdd"/>


//TextView (display) / EditText (input)
<TextView
    android:id="@+id/tvMsg"
    android:layout_width="wrap_content" android:layout_height="wrap_content"
    android:text="HELLO ANDROID!"
    android:textSize="30sp" android:textStyle="bold"
    android:textColor="#0a0" android:textAllCaps="true"
    android:shadowColor="#000" android:shadowDx="4"
    android:shadowDy="4" android:shadowRadius="2"/>

<EditText
    android:id="@+id/email"
    android:layout_width="match_parent" android:layout_height="wrap_content"
    android:inputType="textEmailAddress"/>

//EditText with TextWatcher (validate as user types)

TextView error = findViewById(R.id.length_error_message);
EditText pwd = findViewById(R.id.password_edit_text);

pwd.addTextChangedListener(new TextWatcher() {
    public void beforeTextChanged(CharSequence s, int start, int count, int after) {}
    public void onTextChanged(CharSequence s, int start, int before, int count) {
        error.setVisibility(s.length() < 8 ? View.VISIBLE : View.INVISIBLE);
    }
    public void afterTextChanged(Editable s) {}
});

//ToggleButton / Switch (on–off)

<androidx.appcompat.widget.SwitchCompat
    android:id="@+id/my_switch"
    android:layout_width="wrap_content" android:layout_height="wrap_content"/>

//

SwitchCompat sw = findViewById(R.id.my_switch);
sw.setOnCheckedChangeListener((buttonView, isChecked) -> {
    // handle on/off
});

//RadioGroup / RadioButton (single choice)

<RadioGroup
    android:layout_width="wrap_content" android:layout_height="wrap_content"
    android:orientation="vertical">
    <RadioButton
        android:id="@+id/radio_yes"
        android:text="@string/yes" android:checked="true"
        android:onClick="onRadioButtonClicked"/>
    <RadioButton
        android:id="@+id/radio_no"
        android:text="@string/no" android:onClick="onRadioButtonClicked"/>
</RadioGroup>

//

public void onRadioButtonClicked(View view) {
    switch (view.getId()) {
        case R.id.radio_yes: /* ... */ break;
        case R.id.radio_no:  /* ... */ break;
    }
}


//CheckBox (multi-select)
<CheckBox
    android:id="@+id/checkbox_reading"
    android:layout_width="wrap_content" android:layout_height="wrap_content"
    android:text="@string/reading" android:onClick="onCheckboxClicked"/>

//

public void onCheckboxClicked(View v) {
    boolean checked = ((CheckBox) v).isChecked();
    // handle checked/unchecked
}


//Spinner (drop-down) with ArrayAdapter

<Spinner
    android:id="@+id/spinner_size"
    android:layout_width="wrap_content" android:layout_height="wrap_content"/>

//

<!-- res/values/strings.xml -->
<string-array name="sizes_array">
    <item>Small</item><item>Medium</item>
    <item>Large</item><item>Extra large</item>
</string-array>

//

Spinner sp = findViewById(R.id.spinner_size);
ArrayAdapter<CharSequence> ad = ArrayAdapter.createFromResource(
    this, R.array.sizes_array, android.R.layout.simple_spinner_item);
ad.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
sp.setAdapter(ad);
sp.setOnItemSelectedListener(new AdapterView.OnItemSelectedListener() {
    public void onItemSelected(AdapterView<?> parent, View view, int pos, long id) {
        String item = (String) parent.getItemAtPosition(pos);
        Toast.makeText(this, item, Toast.LENGTH_SHORT).show();
    }
    public void onNothingSelected(AdapterView<?> parent) {}
});


//ProgressBar / SeekBar / RatingBar

<ProgressBar
    android:id="@+id/progress_bar"
    style="@android:style/Widget.ProgressBar.Large"
    android:layout_width="wrap_content" android:layout_height="wrap_content"/>

<SeekBar
    android:id="@+id/seek"
    android:layout_width="match_parent" android:layout_height="wrap_content"
    android:max="10" android:progress="7"/>

<RatingBar
    android:id="@+id/rating"
    android:layout_width="wrap_content" android:layout_height="wrap_content"
    android:numStars="5" android:stepSize="1" android:rating="3"/>

//

SeekBar sb = findViewById(R.id.seek);
sb.setOnSeekBarChangeListener(new SeekBar.OnSeekBarChangeListener() {
    public void onProgressChanged(SeekBar s, int p, boolean fromUser) { /* ... */ }
    public void onStartTrackingTouch(SeekBar s) {}
    public void onStopTrackingTouch(SeekBar s) {}
});

RatingBar rb = findViewById(R.id.rating);
rb.setOnRatingBarChangeListener((bar, rating, fromUser) -> { /* ... */ });

//ImageView (bitmap/vector) + swapping images in code

<ImageView
    android:id="@+id/my_image_view"
    android:layout_width="wrap_content" android:layout_height="wrap_content"
    android:src="@drawable/orange"
    android:contentDescription="@string/orangeImage"/>

//

ImageView iv = findViewById(R.id.my_image_view);
iv.setOnClickListener(v -> {
    Drawable d = ContextCompat.getDrawable(this, R.drawable.pizza);
    iv.setImageDrawable(d);
});


//Vector drawable w/ tint (res/drawable/cake.xml)

<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="64dp" android:height="64dp"
    android:viewportWidth="600" android:viewportHeight="600">
    <path android:fillColor="#000" android:pathData="M300,70 l 0,-70 70,70 0,0 -70,70z"/>
</vector>

//

<ImageView
    android:layout_width="50dp" android:layout_height="50dp"
    android:tint="@color/green"
    android:src="@drawable/cake"/>


//### STYLES AND THEMES###//

//Style (res/values/styles.xml)

<resources>
    <style name="CalcButton">
        <item name="android:textSize">24sp</item>
        <item name="android:textColor">@color/gray</item>
    </style>
</resources>

//

<Button
    android:layout_width="wrap_content" android:layout_height="wrap_content"
    android:text="Calculate" style="@style/CalcButton"/>

//Theme (Material3 Day/Night) + custom colors (res/values/themes.xml)

<resources xmlns:tools="http://schemas.android.com/tools">
    <style name="Theme.MyApp" parent="Theme.Material3.DayNight.NoActionBar">
        <item name="colorPrimary">@color/teal_700</item>
        <item name="colorPrimaryVariant">@color/teal_900</item>
        <item name="colorOnPrimary">@color/white</item>
        <item name="colorSecondary">@color/amber_500</item>
    </style>
</resources>

//Night variant (res/values-night/themes.xml)

<resources>
    <style name="Theme.MyApp" parent="Theme.Material3.DayNight.NoActionBar">
        <!-- dark theme overrides if needed -->
    </style>
</resources>

//Apply theme (AndroidManifest.xml)
<application
    android:theme="@style/Theme.MyApp" ... >
    <!-- or per-activity:
    <activity android:name=".MainActivity" android:theme="@style/Theme.MyApp" /> -->
</application>

//Fullscreen (optional theme tweaks)

<style name="Theme.MyApp" parent="Theme.Material3.DayNight.NoActionBar">
    <item name="android:windowFullscreen">true</item>
    <item name="android:colorBackground">#f0f0ff</item>
    <item name="android:textColor">@color/purple_700</item>
    <item name="android:textSize">24sp</item>
</style>
