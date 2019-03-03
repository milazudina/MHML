package com.example.vitarun;

import android.app.Service;
import android.content.Intent;
import android.os.Handler;
import android.os.IBinder;
import android.speech.tts.TextToSpeech;



import java.util.Locale;

public class TextToSpeechService extends Service implements TextToSpeech.OnInitListener {

    public static final String EXTRA_WORD = "word";
    public static final String EXTRA_MEANING = "meaning";

    private TextToSpeech tts;
    private String word, meaning;
    private boolean isInit;
    private Handler handler;

    @Override
    public void onCreate() {
        super.onCreate();
        tts = new TextToSpeech(getApplicationContext(), this);
        handler = new Handler();
    }

    @Override
    public int onStartCommand(Intent intent, int flags, int startId) {
        handler.removeCallbacksAndMessages(null);

        word = intent.getStringExtra(TextToSpeechService.EXTRA_WORD);
        meaning = intent.getStringExtra(TextToSpeechService.EXTRA_MEANING);

        if (isInit) {
            speak();
        }

        handler.postDelayed(new Runnable() {

            @Override
            public void run() {
                stopSelf();
            }
        }, 15*1000);

        return TextToSpeechService.START_NOT_STICKY;
    }

    @Override
    public void onDestroy() {
        if (tts != null) {
            tts.stop();
            tts.shutdown();
        }
        super.onDestroy();
    }

    @Override
    public void onInit(int status) {
        if (status == TextToSpeech.SUCCESS) {
            int result = tts.setLanguage(Locale.GERMAN);
            if (result != TextToSpeech.LANG_MISSING_DATA && result != TextToSpeech.LANG_NOT_SUPPORTED) {
                speak();
                isInit = true;
            }
        }
    }

    private void speak() {
        if (tts != null) {
            tts.speak(word, TextToSpeech.QUEUE_FLUSH, null);
            tts.speak(meaning, TextToSpeech.QUEUE_ADD, null);
        }
    }

    @Override
    public IBinder onBind(Intent arg0) {
        return null;
    }

}