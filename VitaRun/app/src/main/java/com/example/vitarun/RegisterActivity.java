package com.example.vitarun;

import android.content.Intent;
import android.os.Bundle;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

public class RegisterActivity extends AppCompatActivity implements View.OnClickListener {
    Button bCreateProfile;
    EditText etUsername, etAge, etWeight, etPassword, etNickname;
    TextView tvLoginLink;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_register);
        bCreateProfile = (Button) findViewById(R.id.bCreateProfile);
        etAge = (EditText) findViewById(R.id.etAge);
        etUsername = (EditText) findViewById(R.id.etUsername);
        etNickname = (EditText) findViewById(R.id.etNickname);
        etPassword = (EditText) findViewById(R.id.etPassword);
        etWeight = (EditText) findViewById(R.id.etWeight);
        tvLoginLink = (TextView) findViewById(R.id.tvLoginLink) ;


        bCreateProfile.setOnClickListener(this);
        tvLoginLink.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch(v.getId()) {
            case (R.id.bCreateProfile):

                String username = etUsername.getText().toString();
                String password = etPassword.getText().toString();
                String nickname = etNickname.getText().toString();
                int age = Integer.parseInt(etAge.getText().toString());
                int weight = Integer.parseInt(etWeight.getText().toString());

                User createProfile = new User(username, password, nickname, age, weight);




                break;
            case R.id.tvLoginLink:
                startActivity(new Intent(this, LoginActivity.class));
        }
    }
}
