package org.swkoubou.peppermill.meetingsupport.heataup_animation;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import com.aldebaran.qi.QiCallback;
import com.aldebaran.qi.sdk.Qi;
import com.aldebaran.qi.sdk.object.interaction.Say;


public class MainActivity extends AppCompatActivity {
    private static final String TAG = "SayActivity";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Animations animation = new Animations(this);
        animation.Say();
    }

}