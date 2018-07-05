import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ObservablesExComponent } from './observables-ex.component';

describe('ObservablesExComponent', () => {
  let component: ObservablesExComponent;
  let fixture: ComponentFixture<ObservablesExComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ObservablesExComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ObservablesExComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
