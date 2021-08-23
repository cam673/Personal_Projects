//
//  ViewController.swift
//  Fancy_Hello
//
//  Created by Christopher on 7/27/20.
//  Copyright © 2020 Sharkbite Studios. All rights reserved.
//

import UIKit

class ViewController: UIViewController
{
    @IBOutlet weak var background: UIImageView!
    @IBOutlet weak var imageTitle: UIImageView!
    @IBOutlet weak var welcomeBtn: UIButton!
    override func viewDidLoad()
    {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

    @IBAction func welcomePressed(_ sender: Any)
    {
        background.isHidden = false
        imageTitle.isHidden = false
        welcomeBtn.isHidden = true
    }
    
}

