package org.swkoubou.peppermill.meetingsupport.heataup_animation;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;

import com.aldebaran.qi.sdk.object.actuation.Animate;
import com.aldebaran.qi.sdk.object.actuation.Animation;


// ref. https://android.aldebaran.com/doc/elephant_tutorial.html#elephant-tutorial
public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    @Override
    protected void onStart() {
        super.onStart();

        Animation heatUpAnimation = Animations.HeatUp(this);
        Animate animate = new Animate(this);
        animate.run(heatUpAnimation);
    }
}