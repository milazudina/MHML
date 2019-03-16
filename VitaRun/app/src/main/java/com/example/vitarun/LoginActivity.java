package com.example.vitarun;


import android.content.Context;
import android.content.Intent;
import android.support.design.widget.CoordinatorLayout;
import android.support.design.widget.Snackbar;
import android.support.v4.app.Fragment;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.TextView;
import android.widget.EditText;
import android.widget.Button;

import java.io.IOException;
import java.io.OutputStream;
import java.io.OutputStreamWriter;
import java.io.PrintStream;
import java.net.ConnectException;

public class LoginActivity extends AppCompatActivity implements View.OnClickListener {
    Button bLogin;
    EditText etUsername, etPassword;
    TextView tvNewProfile;
    LocalStore UserLocalStore;
    ServerComms serverComms;
    TextView tvUsername, tvName, tvAge, tvWeight;



    @Override
    protected void onCreate(Bundle savedInstanceState) {
        System.out.println("LoginActivity Created");
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_login);
        bLogin = (Button) findViewById(R.id.bLogin);
        etUsername = (EditText) findViewById(R.id.etUsername);
        etPassword = (EditText) findViewById(R.id.etPassword);
        tvNewProfile = (TextView) findViewById(R.id.tvNewProfile);


        UserLocalStore = new LocalStore(this);

        serverComms = new ServerComms();

        bLogin.setOnClickListener(this);
        tvNewProfile.setOnClickListener(this);


    }

    @Override
    public void onClick(View v) {
        switch(v.getId()){
            case(R.id.bLogin):
                String username_raw = etUsername.getText().toString();
                String attemptPasswordRaw = etPassword.getText().toString();

                String attemptPassword = attemptPasswordRaw.replaceAll(" ", "_");

                String username = username_raw.replaceAll("\\s","");
                int serverResponse = serverComms.login(username, attemptPassword);
                System.out.print("Server Response:" + serverResponse);

                if (serverResponse == 0) {
                    Snackbar sbUsername = Snackbar.make(v, "Incorrect Password", Snackbar.LENGTH_LONG);
                    sbUsername.show();
                    System.out.println("Response Incorrect");
                } else if (serverResponse == -1) {
                    Snackbar sbUsername = Snackbar.make(v, "Username does not exist", Snackbar.LENGTH_LONG);
                    sbUsername.setAction("Create Profile?", new View.OnClickListener() {
                        @Override
                        public void onClick(View v) {
                            startActivity(new Intent(new Intent(getBaseContext(), RegisterActivity.class)));
                            finish();

                        }
                    });
                    sbUsername.show();
                    System.out.println("Response Incorrect");
                } else{

                    Intent returnIntent = new Intent();
                    returnIntent.putExtra("result",username);
                    setResult(LoginActivity.RESULT_OK,returnIntent);

                    finish();
                    System.out.println("Correct Password");

                    SaveSharedPreferences.setUsername(this.getBaseContext(), username);

                    System.out.println(username);

                }
//
//                    Snackbar sbConnection = Snackbar.make(v, "Unable to Connect, check WiFi Settings", Snackbar.LENGTH_LONG);
//                    sbConnection.show();
//                    //throw new ConnectException("Unable to connect to server");


                //User user = new User(null, null, null, 0, 0);

                //UserLocalStore.storeUserData(user);
                //UserLocalStore.setUserLoggedIn(true);

                break;

            case(R.id.tvNewProfile):
                startActivity(new Intent(this, RegisterActivity.class));
                finish();
        }
    }
}
