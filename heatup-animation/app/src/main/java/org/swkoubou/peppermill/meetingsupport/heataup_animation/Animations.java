package org.swkoubou.peppermill.meetingsupport.heataup_animation;

import android.support.v7.app.AppCompatActivity;
import android.util.Log;

import com.aldebaran.qi.QiCallback;
import com.aldebaran.qi.sdk.Qi;
import com.aldebaran.qi.sdk.object.interaction.Say;

public class Animations {
    private static final String TAG = "Animations";

    private AppCompatActivity activity;

    Animations (AppCompatActivity activity) {
        this.activity = activity;
    }

    public void Say () {
        Say say = new Say(this.activity);
        say.run("Hello, world!").then(Qi.onUiThread(new QiCallback<Void>() {
            @Override
            public void onResult(Void ignore) {
                Log.d(TAG, "result on thread " + Thread.currentThread().getName());
            }

            @Override
            public void onError(Throwable error) {
                Log.e(TAG, "error", error);
            }

            @Override
            public void onCancel() {
                Log.w(TAG, "cancel");
            }
        }));
    }
}
