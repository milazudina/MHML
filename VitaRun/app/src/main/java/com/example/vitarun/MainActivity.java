package com.example.vitarun;

import android.app.Activity;
import android.bluetooth.BluetoothAdapter;
import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothGatt;
import android.bluetooth.BluetoothGattCallback;
import android.bluetooth.BluetoothGattCharacteristic;
import android.bluetooth.BluetoothGattDescriptor;
import android.bluetooth.BluetoothGattService;
import android.bluetooth.BluetoothManager;
import android.content.BroadcastReceiver;
import android.content.ComponentName;
import android.content.Context;
import android.content.Intent;
import android.content.ServiceConnection;
import android.content.pm.PackageManager;
import android.location.Address;
import android.os.Build;
import android.os.Handler;
import android.os.IBinder;
import android.provider.Settings;
import android.support.annotation.NonNull;
import android.support.design.widget.BottomNavigationView;
import android.support.design.widget.Snackbar;
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
import android.widget.ImageView;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.UUID;

import static android.bluetooth.BluetoothAdapter.STATE_CONNECTED;
import static android.bluetooth.BluetoothAdapter.STATE_DISCONNECTED;

public class MainActivity extends AppCompatActivity {

    public static HashMap<String, String> stridMACs;
    private static UUID stridServiceUUID;
    private static UUID stridBioCharUUID;

    BluetoothAdapter bluetoothAdapter;

    // Custom class for storing objects necessary for BLE connection.
    StridBLE leftStrid;
    StridBLE rightStrid;

    private DashboardFragment dashboardFragment;
    private RunFragment runFragment;
    private ProfileFragment profileFragment;
    private RecommendationsFragment recommendationsFragment;


    public RunEvent runEvent;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        runEvent = new RunEvent(this);


        stridMACs = new HashMap<>();
        stridMACs.put("0C:1C:57:6E:A1:B9", "left");
        stridMACs.put("F8:36:9B:74:6D:C8", "right");

        // The Stridalyzer Service UUID.
        stridServiceUUID = convertFromInteger(0x1814);
        // The Stridalyser pressure/acc Characteristic UUID.
        stridBioCharUUID = convertFromInteger(0x2A53);

        dashboardFragment = new DashboardFragment();
        runFragment = new RunFragment();
        profileFragment = new ProfileFragment();

        recommendationsFragment = runFragment.recommendationsFragment;


        // Only initialise bluetooth if NOT being run in emulator.
        if (!Build.FINGERPRINT.contains("generic")) {
            InitialiseBluetooth();
            System.out.println("ON PHONE");
        }

        ImageButton bluetooth_button = (ImageButton) findViewById(R.id.bluetooth_icon);
        bluetooth_button.setOnClickListener(new View.OnClickListener() {

            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Scanning for Insoles", 2000)
                        .setAction("Action", null).show();

                RunBLE();
            }
        });

        BottomNavigationView bottomNav = findViewById(R.id.bottom_navigation);
        bottomNav.setOnNavigationItemSelectedListener(navListener);

        getSupportFragmentManager().beginTransaction().replace(R.id.master_fragment_container,
                new DashboardFragment()).commit();
    }


    public void onInputASent(CharSequence input) {
        recommendationsFragment.updateEditText(input);
    }


    public void InitialiseBluetooth() {
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
        bluetoothAdapter = bluetoothManager.getAdapter();

        // Checks if Bluetooth is supported on the device.
        if (bluetoothAdapter == null) {
            Toast.makeText(this, "Bluetooth Not Supported", Toast.LENGTH_SHORT).show();
            finish();
            return;
        }
    }

    public void RunBLE() {

        leftFound = false;
        leftStrid = new StridBLE("0C:1C:57:6E:A1:B9", "left");
        setSoleConnected(false, "left");

        rightFound = false;
        rightStrid = new StridBLE("F8:36:9B:74:6D:C8", "right");
        ;
        setSoleConnected(false, "right");

        // Stop scanning, used in case scan was already being performed.
        bluetoothAdapter.stopLeScan(scanCallback);

        // Handler used to stop scan after a set period of time.
        Handler mHandler = new Handler();
        mHandler.postDelayed(new Runnable() {
            @Override
            public void run() {
                bluetoothAdapter.stopLeScan(scanCallback);
                invalidateOptionsMenu();
            }
        }, 8000);


        // Start the scan.
        bluetoothAdapter.startLeScan(scanCallback);
        System.out.println("Starting Scan");
    }

    boolean leftFound = false;
    boolean rightFound = false;

    private BluetoothAdapter.LeScanCallback scanCallback =
            new BluetoothAdapter.LeScanCallback() {

                @Override
                public void onLeScan(final BluetoothDevice device, int rssi, byte[] scanRecord) {

                    // If a found device's address is equal to the address of an insole.
                    if (stridMACs.keySet().contains(device.getAddress())) {

                        // Determine which insole it is.
                        String side = stridMACs.get(device.getAddress());

                        if (side == "left" && !leftFound) {
                            leftStrid.bleDevice = device;
                            ConnectGatt(leftStrid);
                            leftFound = true;
                            System.out.println("Left Insole Found");

                        } else if (side == "right" && !rightFound) {
                            rightStrid.bleDevice = device;
                            ConnectGatt(rightStrid);
                            rightFound = true;
                            System.out.println("Right Insole Found");
                        }
                    }
                }
            };

    private void ConnectGatt(final StridBLE insole) {
        insole.gatt = insole.bleDevice.connectGatt(this, true, insole.gattCallback);

    }

    private void setSoleConnected(final Boolean connected, final String side) {

        this.runOnUiThread(new Runnable() {
            @Override
            public void run() {
                switch (side) {
                    case "left":
                        ImageView leftSoleIcon = findViewById(R.id.insole_left_icon);

                        if (connected) {
                            leftSoleIcon.setImageResource(R.drawable.vitarun_insoleleft_fill);
                        } else {
                            leftSoleIcon.setImageResource(R.drawable.vitarun_insoleleft);
                        }
                        break;
                    case "right":
                        ImageView rightSoleIcon = findViewById(R.id.insole_right_icon);

                        if (connected) {
                            rightSoleIcon.setImageResource(R.drawable.vitarun_insoleright_fill);
                        } else {
                            rightSoleIcon.setImageResource(R.drawable.vitarun_insoleright);
                        }
                        break;
                }
            }
        });
    }

    private class StridBLE {

        public final String side;
        public String MAC;
        public BluetoothDevice bleDevice;
        public BluetoothGatt gatt;
        public BluetoothGattCallback gattCallback;

        public StridBLE(String MAC, final String side) {
            this.side = side;
            this.MAC = MAC;

            gattCallback = new BluetoothGattCallback() {
                @Override
                public void onConnectionStateChange(BluetoothGatt gatt, int status, int newState) {
                    super.onConnectionStateChange(gatt, status, newState);

                    if (newState == STATE_CONNECTED) {
                        System.out.println(side + " Insole Connected");
                        setSoleConnected(true, side);
                        gatt.discoverServices();
                    } else if (newState == STATE_DISCONNECTED) {
                        System.out.println(side + " Insole Disconnected");
                        setSoleConnected(false, side);
                    }
                }


                @Override
                public void onServicesDiscovered(BluetoothGatt gatt, int status) {
                    super.onServicesDiscovered(gatt, status);

                    BluetoothGattCharacteristic characteristic =
                            gatt.getService(stridServiceUUID)
                                    .getCharacteristic(stridBioCharUUID);

                    gatt.setCharacteristicNotification(characteristic, true);

                    BluetoothGattDescriptor descriptor =
                            characteristic.getDescriptor(convertFromInteger(0x2902));

                    descriptor.setValue(
                            BluetoothGattDescriptor.ENABLE_NOTIFICATION_VALUE);

                    gatt.writeDescriptor(descriptor);
                }

                @Override
                public void onDescriptorWrite(BluetoothGatt gatt, BluetoothGattDescriptor descriptor,
                                              int status) {
                    super.onDescriptorWrite(gatt, descriptor, status);

                    BluetoothGattCharacteristic characteristic =
                            gatt.getService(stridServiceUUID)
                                    .getCharacteristic(stridBioCharUUID);

                    characteristic.setValue(new byte[]{1, 1});
                    gatt.writeCharacteristic(characteristic);
                }

                @Override
                public void onCharacteristicChanged(BluetoothGatt gatt, BluetoothGattCharacteristic
                        characteristic) {
                    super.onCharacteristicChanged(gatt, characteristic);

                    byte[] DataBytes = characteristic.getValue();

                    runEvent.addDataSample(side, DataBytes);

//                        String DataString = new String(DataBytes, StandardCharsets.UTF_16);
//                        System.out.println(DataString);
                }
            }
            ;
        }

    }


    public UUID convertFromInteger(int i) {
        final long MSB = 0x0000000000001000L;
        final long LSB = 0x800000805f9b34fbL;
        long value = i & 0xFFFFFFFF;
        return new UUID(MSB | (value << 32), LSB);
    }

    // NAVIGATION
    private BottomNavigationView.OnNavigationItemSelectedListener navListener =
            new BottomNavigationView.OnNavigationItemSelectedListener() {
                @Override
                public boolean onNavigationItemSelected(@NonNull MenuItem menuItem) {
                    Fragment selectedFragment = null;

                    switch (menuItem.getItemId()) {
                        case R.id.nav_dashboard:
                            selectedFragment = dashboardFragment;
                            break;
                        case R.id.nav_run:
                            selectedFragment = runFragment;
                            break;
                        case R.id.nav_profile:
                            selectedFragment = profileFragment;
                            break;
                    }

                    getSupportFragmentManager().beginTransaction().replace(R.id.master_fragment_container,
                            selectedFragment).commit();

                    return true;
                }
            };
}
