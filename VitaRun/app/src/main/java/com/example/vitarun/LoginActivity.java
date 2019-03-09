package com.example.vitarun;


import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.TextView;
import android.widget.EditText;
import android.widget.Button;

public class LoginActivity extends AppCompatActivity implements View.OnClickListener {
    Button bLogin;
    EditText etUsername, etPassword;
    TextView tvNewProfile;
    LocalStore UserLocalStore;


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


        bLogin.setOnClickListener(this);
        tvNewProfile.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        switch(v.getId()){
            case(R.id.bLogin):
                User user = new User(null, null, null, 0, 0);

                UserLocalStore.storeUserData(user);
                UserLocalStore.setUserLoggedIn(true);

                break;

            case(R.id.tvNewProfile):
                startActivity(new Intent(this, RegisterActivity.class));
        }
    }
}
