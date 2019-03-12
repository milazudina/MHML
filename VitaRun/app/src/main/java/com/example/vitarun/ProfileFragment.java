package com.example.vitarun;

import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.ViewSwitcher;

import java.io.IOException;
import java.io.OutputStreamWriter;

import static android.content.Context.MODE_PRIVATE;


public class ProfileFragment extends Fragment {
    ViewSwitcher mViewSwitcher;
    LocalStore userLocalStore;
    EditText etUsername, etName, etAge, etWeight;
    TextView tvUsername, tvName, tvAge, tvWeight;
    ServerComms serverComms;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_profile, container, false);
        mViewSwitcher = view.findViewById(R.id.swProfileEdit);
        etUsername = (EditText) view.findViewById(R.id.etUserUsername);
        etName = (EditText) view.findViewById(R.id.etUserName);
        etAge = (EditText) view.findViewById(R.id.etUserAge);
        etWeight = (EditText) view.findViewById(R.id.etUserWeight);

        tvUsername = view.findViewById(R.id.tvUserUsername);
        tvName = view.findViewById(R.id.tvUserName);
        tvAge = view.findViewById(R.id.tvUserAge);
        tvWeight = view.findViewById(R.id.tvUserWeight);


        serverComms = new ServerComms();

        Button editButton = (Button) view.findViewById(R.id.bEditProfile);
        Button saveButton = (Button) view.findViewById(R.id.bSaveProfile);
        Button logOutButton = (Button) view.findViewById(R.id.bLogOut);


        System.out.print("Running Profile Fragment");

        // Set User Information

        String getUsername = SaveSharedPreferences.getUserName(getContext());
        if(getUsername.equals("")){

            System.out.print("No username, starting login");

            Intent intent = new Intent(getActivity(), LoginActivity.class);
            startActivity(intent);


        } else {
            System.out.println(getUsername);
            final User getUser = serverComms.getUserDetails(getUsername);
            System.out.println(getUser);
            tvUsername.setText(getUser.username);
            tvAge.setText(String.format("%s", getUser.age));
            tvName.setText(getUser.name);
            tvWeight.setText(String.format("%s", getUser.weight));

            // Edit User Information


            editButton.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    System.out.println("change view"); // some function here
                    mViewSwitcher.showNext();

                    etUsername.setText(getUser.username);
                    etAge.setText(String.format("%s", getUser.age));
                    etName.setText(getUser.name);
                    etWeight.setText(String.format("%s", getUser.weight));


                }
            });

            saveButton.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    System.out.println("change view"); // some function here
                    mViewSwitcher.showNext();

                    String age = etAge.getText().toString();
                    String weight = etWeight.getText().toString();

                    int age_int = Integer.parseInt(age);
                    int weight_int = Integer.parseInt(weight);
                    String username = etUsername.getText().toString();
                    String name = etName.getText().toString();

                    User user = new User(username, getUser.password, name, age_int, weight_int);

                    serverComms.setUserDetails(user);

                    tvUsername.setText(user.username);
                    tvAge.setText(String.format("%s", user.age));
                    tvName.setText(user.name);
                    tvWeight.setText(String.format("%s", user.weight));



                }
            });

            logOutButton.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    SaveSharedPreferences.setUsername(getContext(), "");

                    Intent intent = new Intent(getActivity(), LoginActivity.class);
                    startActivity(intent);


                    //userLocalStore.setUserLoggedIn(false);
                    //userLocalStore.clearUserData();


                }
            });

        }
        return view;
    }
}
