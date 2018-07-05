import { Component, OnInit } from '@angular/core';
import {fromEvent} from 'rxjs';

@Component({
  selector: 'app-websocket',
  templateUrl: './websocket.component.html',
  styleUrls: ['./websocket.component.css']
})
export class WebsocketComponent implements OnInit {
	ws = fromEvent(new WebSocket('wss://echo.websocket.org'), 'message');

  constructor() { }

  ngOnInit() {
  	let subscription = this.ws.subscribe((val)=>console.log('echo from server', val));
  	// In order to invoke send of ws pass value to next of this Observable
  	subscription.next('{"a": "b"}')
  }

}
