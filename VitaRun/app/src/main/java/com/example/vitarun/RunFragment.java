package com.example.vitarun;

import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentTransaction;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;

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

//    public void newRun() {
//        getChildFragmentManager().beginTransaction().replace(R.id.run_transportControl_container,
//                new TransportControlFragment()).commit();
//
//    }
}

