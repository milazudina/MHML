package com.example.vitarun;

import android.app.Service;
import android.content.Intent;
import android.os.IBinder;

public class TextToSpeechService extends Service {
    public TextToSpeechService() {
    }

    @Override
    public IBinder onBind(Intent intent) {
        // TODO: Return the communication channel to the service.
        throw new UnsupportedOperationException("Not yet implemented");
    }
}
