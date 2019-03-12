package com.example.vitarun;


import android.app.Activity;
import android.content.Context;
import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentTransaction;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ViewSwitcher;


public class TransportControlFragment extends Fragment {
    ViewSwitcher mViewSwitcher;

    RunFragment runFragment;

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        View view = inflater.inflate(R.layout.fragment_transport_control, container, false);
        mViewSwitcher = view.findViewById(R.id.profileSwitcher);
        Button startButton = (Button) view.findViewById(R.id.start_run_button);
        Button stopButton = (Button) view.findViewById(R.id.stop_button);
        Button pauseButton = (Button) view.findViewById(R.id.pause_button);

        runFragment = (RunFragment) getParentFragment();

        startButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v ) {

                runFragment.callback.StartRun();

                mViewSwitcher.showNext();
//                System.out.println("change view complete?");
            }
        });

        pauseButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                runFragment.callback.PauseRun();

            }
        });

        stopButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
//                System.out.println("change view"); // some function here
                // mViewSwitcher.setDisplayedChild(0);

                runFragment.callback.EndRun();

                mViewSwitcher.showNext();
//                System.out.println("change view complete?");
            }
        });
        return view;
    }

}

