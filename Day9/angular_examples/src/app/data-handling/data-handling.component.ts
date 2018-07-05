import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-data-handling',
  templateUrl: './data-handling.component.html',
  styleUrls: ['./data-handling.component.css']
})
export class DataHandlingComponent implements OnInit {

	// Single data member to show on Template
  data:string="some_data_to_show_on_page";

  // Bunch of data members to show on Template
  bunch_of_data=[1,2,3,4];

  // Object to show on Template
  some_object:object={property1: "Value1", property2: "Value2"};

  // logit to access console.log inside our template
  logit=(arg)=>console.log(arg);

  some_variable:string;

  // Two way bound variable
  two_way_bound:string;

  // Two way bound style_name
  classes={'class1':false, 'class2':true};

  constructor() { }

  ngOnInit() {
  }

  changeSomeVariable(arg) {
  	this.some_variable=arg;
  }

}
