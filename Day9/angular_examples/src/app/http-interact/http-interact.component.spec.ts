import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { HttpInteractComponent } from './http-interact.component';

describe('HttpInteractComponent', () => {
  let component: HttpInteractComponent;
  let fixture: ComponentFixture<HttpInteractComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ HttpInteractComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(HttpInteractComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
