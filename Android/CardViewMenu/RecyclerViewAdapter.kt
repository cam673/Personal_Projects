package com.example.cardviewmenu

import android.content.Intent
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.view.menu.ActionMenuItemView
import androidx.core.content.ContextCompat.startActivity
import androidx.recyclerview.widget.RecyclerView

class RecyclerViewAdapter: RecyclerView.Adapter<RecyclerViewAdapter.ViewHolder>()
{
    private val itemTitles = arrayOf("Bottles", "Cow", "Egg", "Flowers")
    private val itemDetails = arrayOf("Bottle recycling guide.", "Learn about the different breeds of cows from all parts of the world",
    "The quintessential superfood of early mornings, learn more here.", "Learn about the different species of flowers.")
    private val itemImages = intArrayOf(
        R.drawable.bottle,
        R.drawable.cow,
        R.drawable.egg,
        R.drawable.flower
    )

    inner class ViewHolder(itemView: View): RecyclerView.ViewHolder(itemView)
    {
        var image: ImageView
        var textTitle: TextView
        var textDes: TextView
        lateinit var edit: Button

        init {
            image = itemView.findViewById(R.id.item_image)
            textTitle = itemView.findViewById(R.id.item_title)
            textDes = itemView.findViewById(R.id.item_details)
            edit = itemView.findViewById(R.id.btn_temp)

            edit.setOnClickListener {
                Toast.makeText(itemView.context, "Edit button clicked", Toast.LENGTH_LONG).show()
            }
        }

    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val v = LayoutInflater.from(parent.context)
            .inflate(R.layout.rv_model, parent, false)
        return ViewHolder(v)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.textTitle.text = itemTitles [position]
        holder.textDes.text = itemDetails [position]
        holder.image.setImageResource(itemImages [position])

        holder.itemView.setOnClickListener { v: View ->
            Toast.makeText(v.context, "Bio item selected", Toast.LENGTH_LONG).show()
            val intent = Intent(v.context, CardSelect::class.java)

            val t1 = itemTitles[position]
            val t2 = itemDetails[position]
            val p1 = itemImages[position]

            intent.putExtra("title", t1)
            intent.putExtra("desc", t2)
            intent.putExtra("picture", p1)

            v.context.startActivity(intent)
        }

    }

    override fun getItemCount(): Int {
        return itemTitles.size
    }

}