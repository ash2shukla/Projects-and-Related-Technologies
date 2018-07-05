import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-http-interact',
  templateUrl: './http-interact.component.html',
  styleUrls: ['./http-interact.component.css']
})
export class HttpInteractComponent implements OnInit {

	API_URL = 'https://jsonplaceholder.typicode.com/posts/1';
  
  constructor(private http: HttpClient) { }

  ngOnInit() {
  	this.http.get(this.API_URL).subscribe((value)=>console.log(value));
  	// Although it can be used as it is inside a component but APIs interactions are
  	// often distributed over the components which will make this HttpClient access
  	// redundant. Thus we always put the logic of accessing APIs in services.

  }

}
