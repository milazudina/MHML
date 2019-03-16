package com.example.vitarun;

import android.content.Intent;
import android.os.Bundle;
import android.support.design.widget.Snackbar;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class RegisterActivity extends AppCompatActivity implements View.OnClickListener {
    Button bCreateProfile;
    EditText etUsername, etAge, etWeight, etPassword, etName;
    TextView tvLoginLink;
    ServerComms serverComms;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        bCreateProfile = (Button) findViewById(R.id.bCreateProfile);

        etAge = (EditText) findViewById(R.id.etAge);
        etUsername = (EditText) findViewById(R.id.etUsername);
        etName = (EditText) findViewById(R.id.etName);
        etPassword = (EditText) findViewById(R.id.etPassword);
        etWeight = (EditText) findViewById(R.id.etWeight);

        tvLoginLink = (TextView) findViewById(R.id.tvLoginLink) ;
        serverComms = new ServerComms();

        bCreateProfile.setOnClickListener(this);
        tvLoginLink.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch(v.getId()) {
            case (R.id.bCreateProfile):

                String username = etUsername.getText().toString();
                String password_raw = etPassword.getText().toString();
                String name_raw = etName.getText().toString();

                String password = password_raw.replaceAll(" ","_");
                String name = name_raw.replaceAll(" ","_");


                int age = Integer.parseInt(etAge.getText().toString());
                int weight = Integer.parseInt(etWeight.getText().toString());

                if(username.contains(" ")){
                    Snackbar sbUsernameSpaces = Snackbar.make(v, "Username may not contain spaces. Try using \"_\"", Snackbar.LENGTH_LONG);
                    sbUsernameSpaces.show();

                } else {

                    User createProfile = new User(username, password, name, age, weight);
                    boolean created = serverComms.createProfile(username, password, name, age, weight);
                    System.out.println(createProfile);
                    System.out.println("New profile created: " + created);
                    if(created){
                        System.out.println("Successful Creation");
                        finish();

                    } else {
                        Snackbar sbInvalidDetails = Snackbar.make(v, "Details Invalid", Snackbar.LENGTH_LONG);
                        sbInvalidDetails.show();
                        System.out.println("Unsuccessful Creation");
                    }
                }
                break;
            case R.id.tvLoginLink:
                startActivity(new Intent(this, LoginActivity.class));
                finish();
        }
    }
}
