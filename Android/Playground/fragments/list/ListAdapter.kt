package com.example.playground.fragments.list

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import androidx.navigation.findNavController
import androidx.recyclerview.widget.RecyclerView
import com.example.playground.R
import com.example.playground.model.User
import kotlinx.android.synthetic.main.custom_row.view.*

class ListAdapter: RecyclerView.Adapter<ListAdapter.MyViewHolder>()
{
    private var userList = emptyList<User>()

    class MyViewHolder(itemView: View): RecyclerView.ViewHolder(itemView)
    {
        //
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): MyViewHolder
    {
        return MyViewHolder(LayoutInflater.from(parent.context).inflate(R.layout.custom_row, parent, false))
    }


    override fun getItemCount(): Int
    {
        return userList.size
    }

    override fun onBindViewHolder(holder: MyViewHolder, position: Int)
    {
        val currentItem = userList[position]
        holder.itemView.tv_listID.text = currentItem.id.toString()
        holder.itemView.tv_listFName.text = currentItem.firstName
        holder.itemView.tv_listLName.text = currentItem.lastName
        holder.itemView.tv_listAge.text = currentItem.age.toString()

        holder.itemView.rowLayout.setOnClickListener{
            val action = ListFragmentDirections.actionListFragmentToUpdateFragment(currentItem)
            holder.itemView.findNavController().navigate(action)
        }
    }

    fun setData(user: List<User>)
    {
        this.userList = user
        notifyDataSetChanged()
    }
}