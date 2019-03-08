package com.example.vitarun;

import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.ViewSwitcher;

public class ProfileFragment extends Fragment {
    ViewSwitcher mViewSwitcher;



    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_profile, container, false);
        mViewSwitcher = view.findViewById(R.id.swProfileEdit);

        Button editButton = (Button) view.findViewById(R.id.bEditProfile);
        Button saveButton = (Button) view.findViewById(R.id.bSaveProfile);

        editButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v ) {
                System.out.println("change view"); // some function here
                mViewSwitcher.showNext();
                System.out.println("change view complete?");


            }
        });

        saveButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v ) {
                System.out.println("change view"); // some function here
                mViewSwitcher.showNext();
                System.out.println("change view complete?");


            }
        });

    return view;

    }
}
