package com.example.vitarun;

import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v4.app.FragmentManager;
import android.support.v4.app.FragmentTransaction;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;


public class TransportControlFragment extends Fragment {

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_transport_control, container, false);
        Button button = (Button) view.findViewById(R.id.stop_button);
        button.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                FragmentManager fm = getFragmentManager();
                StartRunFragment f = (StartRunFragment) fm.findFragmentById(R.id.transport_control_fragment);
                if (f == null) {
                    getFragmentManager()
                            .beginTransaction()
                            .replace(R.id.run_transportControl_container, new StartRunFragment())
                            .commit();
                }
            }
        });

        return view;
    }


}
