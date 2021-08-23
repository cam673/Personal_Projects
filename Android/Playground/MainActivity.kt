package com.example.playground

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.Toast
import kotlinx.android.synthetic.main.activity_main.*
import java.util.*

class MainActivity : AppCompatActivity()
{

    override fun onCreate(savedInstanceState: Bundle?)
    {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        //Send user to recipe prototype
        btn_recipe.setOnClickListener {
            Intent(this, Proto_Recipe::class.java).also {
                startActivity(it)
            }
        }

        //Send user to database prototype
        btn_database.setOnClickListener {
            Intent(this, RoomDemo::class.java).also {
                startActivity(it)
            }
        }
    }
}
