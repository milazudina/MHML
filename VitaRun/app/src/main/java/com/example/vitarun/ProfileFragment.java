package com.example.vitarun;

import android.content.Intent;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ViewSwitcher;


public class ProfileFragment extends Fragment {
    ViewSwitcher mViewSwitcher;
    LocalStore userLocalStore;
    EditText etUsername, etNickname, etAge, etWeight;
    ServerComms serverComms;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_profile, container, false);



        mViewSwitcher = view.findViewById(R.id.swProfileEdit);
        etUsername = (EditText) view.findViewById(R.id.etUsername);
        etNickname = (EditText) view.findViewById(R.id.etUserEmail);
        etAge = (EditText) view.findViewById(R.id.etUserAge);
        etWeight = (EditText) view.findViewById(R.id.etUserWeight);

        serverComms = new ServerComms();

        Button editButton = (Button) view.findViewById(R.id.bEditProfile);
        Button saveButton = (Button) view.findViewById(R.id.bSaveProfile);
        Button logOutButton = (Button) view.findViewById(R.id.bLogOut);

        // Edit User Information


        editButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v ) {
                System.out.println("change view"); // some function here
                mViewSwitcher.showNext();


            }
        });

        saveButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v ) {
                System.out.println("change view"); // some function here
                mViewSwitcher.showNext();

                String age = etAge.getText().toString();
                String weight = etWeight.getText().toString();

                int age_int = Integer.parseInt(age);
                int weight_int = Integer.parseInt(weight);
                String username = etUsername.getText().toString();
                String nickname = etNickname.getText().toString();

                User user = new User(username,"", etNickname.getText().toString(), age_int, weight_int);

                serverComms.setUserDetails(user);


            }
        });

        logOutButton.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v ) {
                Intent intent = new Intent(getActivity(), LoginActivity.class);
                startActivity(intent);
                //userLocalStore.setUserLoggedIn(false);
                //userLocalStore.clearUserData();


            }
        });


        return view;

    }
}
