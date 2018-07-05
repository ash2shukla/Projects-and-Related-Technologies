import { Injectable } from '@angular/core';
import { Observable, of, from } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class SomeDependencyService {
	x = [];
  constructor() { }

  getMockData():Observable<any> {
		return from(this.x);
  }
}
