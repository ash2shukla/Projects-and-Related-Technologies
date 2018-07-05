import { Component, OnInit } from '@angular/core';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-observables-ex',
  templateUrl: './observables-ex.component.html',
  styleUrls: ['./observables-ex.component.css']
})
export class ObservablesExComponent implements OnInit {
	x:number;
	// Observable is a data stream that will be observed
	demo_obs = new Observable((observer) => {
		// observer is the one who wants to observe this data stream
		let ct = 1;
		setInterval(()=>{observer.next(ct); ct++; if(ct==10) observer.complete();}, 1000);
		let unsubscribe= () =>{console.log('Unsubscribed')}
		return {unsubscribe};
	});

  constructor() { }

  ngOnInit() {
  	this.demo_obs.subscribe({
  														next:(val)=>{this.x=val},
  														error: (err)=>{console.log(err);},
  														complete:()=>{console.log('Completed');}
  													});

  }

}
