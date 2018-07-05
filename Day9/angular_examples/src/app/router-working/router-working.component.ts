import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-router-working',
  templateUrl: './router-working.component.html',
  styleUrls: ['./router-working.component.css']
})
export class RouterWorkingComponent implements OnInit {

	constructor(
  	private router: Router,
	) {}
  ngOnInit() {
  	console.log(this.router.snapshot);
  	// this.router.navigate(['whatever path']);
  }

}
