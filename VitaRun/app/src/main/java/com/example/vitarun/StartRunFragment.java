package com.example.vitarun;


import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;


/**
 * A simple {@link Fragment} subclass.
 */
public class StartRunFragment extends Fragment {

    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {

        View view = inflater.inflate(R.layout.fragment_start_run, container, false);
        Button button = (Button) view.findViewById(R.id.start_run_button);
        button.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
               System.out.println("click"); // some function here
                // this doesnt work! below
             //  RunFragment runFragment = new RunFragment();
             //  runFragment.newRun();
            }
        });
        return view;

    }
    public void startRun(){


    }

}
