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
    EditText etName, etAge, etWeight;
    TextView tvUsername, tvName, tvAge, tvWeight;
    ServerComms serverComms;

    static final int GET_LOGGED_IN_USER = 0;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_profile, container, false);
        mViewSwitcher = view.findViewById(R.id.swProfileEdit);
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
            startActivityForResult(intent, GET_LOGGED_IN_USER);


        } else {
            System.out.println(getUsername);

            // Edit User Information
            final User getUser = serverComms.getUserDetails(getUsername);

            setContents(getUser);

            editButton.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    System.out.println("change view"); // some function here
                    mViewSwitcher.showNext();

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
                    String name = etName.getText().toString();

                    User user = new User(getUser.username, getUser.password, name, age_int, weight_int);

                    serverComms.setUserDetails(user);
                    setContents(user);

                }
            });

            logOutButton.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    SaveSharedPreferences.setUsername(getContext(), "");

                    Intent intent = new Intent(getActivity(), LoginActivity.class);
                    startActivityForResult(intent, GET_LOGGED_IN_USER);


                    System.out.print("LOGIN ACTIVITY FINISHED");
                    //userLocalStore.setUserLoggedIn(false);
                    //userLocalStore.clearUserData();
                }
            });

        }
        return view;
    }

    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data) {

        if (requestCode == 0) {
            if(resultCode == LoginActivity.RESULT_OK){
                String result=data.getStringExtra("result");
                final User user = serverComms.getUserDetails(result);

                setContents(user);
            }
        }
    }//onActivityResult


    public void setContents(User user){
        System.out.println("Set Contents to:"+user);
        tvUsername.setText(user.username);
        tvAge.setText(String.format("%s", user.age));
        tvName.setText(user.name);
        tvWeight.setText(String.format("%s", user.weight));

    }
}
