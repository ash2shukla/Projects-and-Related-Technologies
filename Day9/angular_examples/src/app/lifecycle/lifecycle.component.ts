import { Component, OnInit, OnDestroy, OnChanges, Input, Output, EventEmitter} from '@angular/core';

@Component({
  selector: 'app-lifecycle',
  templateUrl: './lifecycle.component.html',
  styleUrls: ['./lifecycle.component.css']
})
export class LifecycleComponent implements OnInit, OnDestroy, OnChanges {
	@Input()
	input_from_others:string;

	@Output()
	event_to_others = new EventEmitter();

  constructor() { 
  	console.log('Inside Constructor');
  }

  ngOnInit() {
  	console.log('Inside Init');
  }

  ngOnDestroy() {
  	console.log('Inside Destroy');
  }

  ngOnChanges(change) {
  	console.log('Inside Changes');
  	console.log(change);
  }

}