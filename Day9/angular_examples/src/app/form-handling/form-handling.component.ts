import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-form-handling',
  templateUrl: './form-handling.component.html',
  styleUrls: ['./form-handling.component.css']
})
export class FormHandlingComponent implements OnInit {
	logit=(value)=>console.log(value);

	xform = new FormGroup ({
    inputx1: new FormControl('', [Validators.required, Validators.maxLength(20)]),
    inputx2: new FormControl('', [])
  });

  constructor() { }

  ngOnInit() {
  }
}
