// Basic Skeleton + Launcher//

<manifest package="com.zybooks.pizzaparty">
  <application
    android:icon="@mipmap/ic_launcher"
    android:label="@string/app_name"
    android:theme="@style/AppTheme.PizzaParty">
    <activity android:name=".MainActivity" android:exported="true">
      <intent-filter>
        <action android:name="android.intent.action.MAIN"/>
        <category android:name="android.intent.category.LAUNCHER"/>
      </intent-filter>
    </activity>
  </application>
</manifest>

//Locking Orientation//

<activity
  android:name=".MainActivity"
  android:exported="true"
  android:screenOrientation="portrait"/>

//Hardware/software features//
//Mark optional using False//

<uses-feature android:name="android.hardware.bluetooth"/>
<uses-feature android:name="android.hardware.camera" android:required="false"/>
<uses-feature android:name="android.software.backup"/>

//Request Permissions//
<uses-permission android:name="android.permission.CAMERA"/>
<uses-permission android:name="android.permission.CALL_PHONE"/>
<uses-permission android:name="android.permission.READ_CONTACTS"/>

//Gradle testing//
android {
  defaultConfig {
    testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
  }
}

dependencies {
  testImplementation 'junit:junit:4.12'
  androidTestImplementation 'androidx.test.ext:junit:1.1.3'
  androidTestImplementation 'androidx.test.espresso:espresso-core:3.4.0'
}
    //Mock android dependencies//
    dependencies {
    testImplementation 'org.mockito:mockito-core:3.6.28'
    }

//Parameterize string resource//
<!-- res/values/strings.xml -->
<string name="total_pizzas_num">Total pizzas: %d</string>

//
getstring(R.string.total_pizzas_num, totalPizzas) replaces %d .
//

//Encapsulation //

// PizzaCalculator.java
public class PizzaCalculator {
  public enum HungerLevel { LIGHT, MEDIUM, RAVENOUS }
  public static final int SLICES_PER_PIZZA = 8;
  private HungerLevel mHungerLevel; private int mPartySize;

  public PizzaCalculator(int partySize, HungerLevel level) {
    setHungerLevel(level); setPartySize(partySize);
  }
  public void setPartySize(int partySize) { if (partySize >= 0) mPartySize = partySize; }
  public int getTotalPizzas() {
    int slicesPerPerson = (mHungerLevel==HungerLevel.LIGHT?2:
                           mHungerLevel==HungerLevel.MEDIUM?3:4);
    return (int)Math.ceil(mPartySize * slicesPerPerson / (double) SLICES_PER_PIZZA);
  }
}

//Controller//
public void calculateClick(View view) {
  int numAttend;
  try {
    numAttend = Integer.parseInt(mNumAttendEditText.getText().toString());
  } catch (NumberFormatException ex) { numAttend = 0; }

  int checkedId = mHowHungryRadioGroup.getCheckedRadioButtonId();
  PizzaCalculator.HungerLevel level = PizzaCalculator.HungerLevel.RAVENOUS;
  if (checkedId == R.id.light_radio_button) level = PizzaCalculator.HungerLevel.LIGHT;
  else if (checkedId == R.id.medium_radio_button) level = PizzaCalculator.HungerLevel.MEDIUM;

  int totalPizzas = new PizzaCalculator(numAttend, level).getTotalPizzas();
  mNumPizzasTextView.setText(getString(R.string.total_pizzas_num, totalPizzas));
}

//JUNIT TESTING//

//Basic Test
@Test
public void testSumArray() {
  int sum = ArrayLibrary.sumArray(new int[]{4,2,5});
  assertEquals(11, sum);
}
    //@Test marks a test; assertEquals verifies expected vs actual

//Lifecycle annotations
@Before public void setUp() { /* runs before each test */ }
@After  public void tearDown() { /* runs after each test */ }
    //Prepares and cleans up per test

//Common Assertions:

assertTrue(cond); assertFalse(cond);
assertEquals(exp, act); assertNotEquals(a, b);
assertArrayEquals(a1, a2);
assertNull(obj); assertNotNull(obj);
assertSame(o1, o2); assertNotSame(o1, o2);
// assertThat(num, is(5)); etc.
    //Verifies boolean, equality, arrays, nullability, identity, matchers

//Hashmap Testing

public class UnitTests {
  private HashMap<String,Integer> mHashMap;

  @Before public void doBeforeEachTest() { mHashMap = new HashMap<>(); }

  @Test public void testMapContainsKey() {
    mHashMap.put("key 1", 123);
    assertTrue(mHashMap.containsKey("key 1"));
  }

  @Test public void testMapSize() {
    assertEquals(0, mHashMap.size());
    mHashMap.put("key 1", 123);
    mHashMap.put("key 2", 456);
    assertEquals(2, mHashMap.size());
  }
}
    //Multiple tests and setups per test

//MOCKITO//

//Runner, mock field, Temporary Folder
@RunWith(MockitoJUnitRunner.class)
public class ExampleUnitTest {
  @Mock Context mMockContext;

  @Rule public TemporaryFolder mTempFolder = new TemporaryFolder();
  // when(mMockContext.openFileOutput(...)).thenReturn(new FileOutputStream(file));
}
    //Create mock context and temp files for file I/O tests.

//Full safe-to-file test
when(mMockContext.openFileOutput(ToDoList.FILENAME, Context.MODE_PRIVATE))
    .thenReturn(new FileOutputStream(writeFile));
// ...write list, read both files, assertArrayEquals(expectedBytes, actualBytes);
    //Verifies exact file output

//Mock simple GetString
when(mMockContext.getString(R.string.app_name)).thenReturn("app name");
    //Returns string during local test

//INSTRUMENT TESTS//

//Get real Context//
@RunWith(AndroidJUnit4.class)
public class ExampleInstrumentedTest {
  @Test
  public void testFileSaved() throws Exception {
    Context appContext =
      androidx.test.platform.app.InstrumentationRegistry
        .getInstrumentation().getTargetContext();

    File file = new File(appContext.getFilesDir(), ToDoList.FILENAME);
    file.delete(); assertFalse(file.exists());

    new ToDoList(appContext).saveToFile();
    assertTrue(file.exists());
  }
}
    //Use AndroidJUnit4 runner and Instrumentation; access app Context and storage.
