package com.example.cardviewmenu

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import kotlinx.android.synthetic.main.activity_card_select.*

class CardSelect : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_card_select)

        var intent = intent
        var text1 = intent.getStringExtra("title")
        var text2 = intent.getStringExtra("desc")
        var pic1 = intent.getIntExtra("picture", 0)

        tv_title.text = text1
        tv_desc.text = text2
        iv_pic.setImageResource(pic1)
    }
}
