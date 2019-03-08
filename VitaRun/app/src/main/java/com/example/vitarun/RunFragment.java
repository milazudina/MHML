package com.example.vitarun;

import android.app.Activity;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentTransaction;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

import java.util.ArrayList;
import java.util.HashMap;

public class RunFragment extends Fragment {

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        getChildFragmentManager().beginTransaction().replace(R.id.run_reccomendation_container,
                new ReccomendationsFragment()).commit();
        getChildFragmentManager().beginTransaction().replace(R.id.run_transportControl_container,
                new TransportControlFragment()).commit();

        getChildFragmentManager().beginTransaction().replace(R.id.run_title_container,
                new RunTitleFragment()).commit();

        return inflater.inflate(R.layout.fragment_run, container, false);

    }

    private HashMap<String, BluetoothLeService> BleServices;

    public void setBleServices(HashMap<String, BluetoothLeService> _BleServices)
    {
        this.BleServices = _BleServices;

        for (String MAC : BleServices.keySet()) {
            System.out.println(MAC);
        }
    }

    RunEvent runEvent;

    public void StartRun()
    {
//        runEvent = new RunEvent();
    }

    public void PauseRun()
    {
        runEvent.PauseRunEvent();
    }

    public void StopRun()
    {
        runEvent.EndRunEvent();
    }

}

