import { Component, OnInit } from '@angular/core';
import { SomeDependencyService } from '../some-dependency.service';

@Component({
  selector: 'app-dep-inject',
  templateUrl: './dep-inject.component.html',
  styleUrls: ['./dep-inject.component.css']
})
export class DepInjectComponent implements OnInit {
	/*
		Dependency Injection is implemented in angular using injectables.
		A prime usage of Injectables is in Services.
		A reference to that class can be used in each of the componenets consistently.
	*/
  constructor(private sds: SomeDependencyService) { 
  	/* We could also have declared it globally but it makes more sense to inject the
  	   dependency locally to a class using private */
  }

  ngOnInit() {
  	let observable = this.sds.getMockData();
  	this.sds.x.push(1);
  	this.sds.x.push(2);
  	this.sds.x.push(3);
  	observable.subscribe((value)=> console.log(value));

  }

}
