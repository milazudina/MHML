package com.example.vitarun;

import android.app.Activity;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothManager;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.ServiceConnection;
import android.content.pm.PackageManager;
import android.os.Build;
import android.os.Handler;
import android.os.IBinder;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.v4.app.Fragment;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.MenuItem;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;

public class MainActivity extends AppCompatActivity {

    // Use this array to store the MAC addresses of the insoles.
    public String[] stridMACs = {"0C:1C:57:6E:A1:B9", "F8:36:9B:74:6D:C8"};

    private boolean mScanning;
    Handler mHandler;

    private ArrayList<BluetoothDevice> mLeDevices;
    private BluetoothAdapter mBluetoothAdapter;

    private static final int REQUEST_ENABLE_BT = 1;

    // Stops scanning after 8 seconds.
    private static final long SCAN_PERIOD = 8000;

    private HashMap<String, BluetoothLeService> mBleServices;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        setContentView(R.layout.activity_main);


        mLeDevices = new ArrayList<>();
        mHandler = new Handler();
        mBleServices = new HashMap<>();

        // Only initialise bluetooth if not being run in emulator.
        if (!Build.FINGERPRINT.contains("generic")) {
            InitialiseBluetooth();
            System.out.println("ON PHONE");
        }

        ImageButton bluetooth_button =(ImageButton)findViewById(R.id.bluetooth_icon);
        bluetooth_button.setOnClickListener(new View.OnClickListener()  {

            public void onClick(View v)  {
                ConnectStridalyzers();
            }
        });

        mLeDevices = new ArrayList<>();
        mHandler = new Handler();


        BottomNavigationView bottomNav = findViewById(R.id.bottom_navigation);
        bottomNav.setOnNavigationItemSelectedListener(navListener);

        getSupportFragmentManager().beginTransaction().replace(R.id.master_fragment_container,
                new DashboardFragment()).commit();
    }

    public void InitialiseBluetooth()
    {
        // Bluetooth Stuff
        // Use this check to determine whether BLE is supported on the device.  Then you can
        // selectively disable BLE-related features.
        if (!getPackageManager().hasSystemFeature(PackageManager.FEATURE_BLUETOOTH_LE)) {
            Toast.makeText(this, "BLE Not Supported", Toast.LENGTH_SHORT).show();
            finish();
        }

        // Initializes a Bluetooth adapter.  For API level 18 and above, get a reference to
        // BluetoothAdapter through BluetoothManager.
        final BluetoothManager bluetoothManager =
                (BluetoothManager) getSystemService(Context.BLUETOOTH_SERVICE);
        mBluetoothAdapter = bluetoothManager.getAdapter();

        // Checks if Bluetooth is supported on the device.
        if (mBluetoothAdapter == null) {
            Toast.makeText(this, "Bluetooth Not Supported", Toast.LENGTH_SHORT).show();
            finish();
            return;
        }
    }

    @Override
    protected void onActivityResult(int requestCode, int resultCode, Intent data) {
        // User chose not to enable Bluetooth.
        if (requestCode == REQUEST_ENABLE_BT && resultCode == Activity.RESULT_CANCELED) {
            finish();
            return;
        }
        super.onActivityResult(requestCode, resultCode, data);
    }

    public void ConnectStridalyzers()
    {
        for (BluetoothLeService service : mBleServices.values()) {
            service.disconnect();
        }
        mBleServices = new HashMap<>();
        mLeDevices.clear();

        System.out.println("Searching");
        scanLeDevice(true);
    }


    private void scanLeDevice(final boolean enable) {
        if (enable) {
            // Stops scanning after a pre-defined scan period.
            mHandler.postDelayed(new Runnable() {
                @Override
                public void run() {
                    mScanning = false;
                    mBluetoothAdapter.stopLeScan(mLeScanCallback);
                    invalidateOptionsMenu();
                }
            }, SCAN_PERIOD);

            mScanning = true;
            mBluetoothAdapter.startLeScan(mLeScanCallback);
        } else {
            mScanning = false;
            mBluetoothAdapter.stopLeScan(mLeScanCallback);
        }
        invalidateOptionsMenu();
    }

    // Device scan callback.
    private BluetoothAdapter.LeScanCallback mLeScanCallback =
            new BluetoothAdapter.LeScanCallback() {

                @Override
                public void onLeScan(final BluetoothDevice device, int rssi, byte[] scanRecord) {
                    runOnUiThread(new Runnable() {
                        @Override
                        public void run() {

                            if (Arrays.asList(stridMACs).contains(device.getAddress()))
                            {
                                CreateBleService(device.getAddress());
                            }
                        }

                        @Override
                        protected void finalize() throws Throwable {
                            super.finalize();
                        }
                    });
                }
            };


    public void CreateBleService(String Address)
    {
        if (!mBleServices.containsKey(Address)) {
            BluetoothLeService service = new BluetoothLeService();
            if (service.connect(Address)) {
                System.out.println(String.format("Connecting to Service %s", Address));
                mBleServices.put(Address, service);
            }
        }
    }


    // NAVIGATION
    private BottomNavigationView.OnNavigationItemSelectedListener navListener =
            new BottomNavigationView.OnNavigationItemSelectedListener() {
                @Override
                public boolean onNavigationItemSelected(@NonNull MenuItem menuItem) {
                    Fragment selectedFragment = null;

                    switch (menuItem.getItemId()) {
                        case R.id.nav_dashboard:
                            selectedFragment = new DashboardFragment();
                            break;
                        case R.id.nav_run:
                            selectedFragment = new RunFragment();
                            break;
                        case R.id.nav_profile:
                            selectedFragment = new ProfileFragment();
                            break;
                    }

                    getSupportFragmentManager().beginTransaction().replace(R.id.master_fragment_container,
                            selectedFragment).commit();

                    return true;
                }
            };
}
