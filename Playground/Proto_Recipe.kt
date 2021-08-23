package com.example.playground

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.ImageView
import androidx.fragment.app.Fragment
import androidx.viewpager2.widget.ViewPager2
import kotlinx.android.synthetic.main.activity_proto__recipe.*

class Proto_Recipe : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?)
    {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_proto__recipe)

        val viewPager: ViewPager2 = findViewById(R.id.viewPager)

        val fragmentList: ArrayList<Fragment> = arrayListOf(
            recipe_intro(),
            recipe_parts(),
            recipe_steps()
        )

        val adapter = ViewPagerAdapter(fragmentList, this)
        viewPager.adapter = adapter
    }
}
