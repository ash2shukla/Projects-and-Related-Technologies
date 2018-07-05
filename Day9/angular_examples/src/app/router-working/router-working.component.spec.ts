import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { RouterWorkingComponent } from './router-working.component';

describe('RouterWorkingComponent', () => {
  let component: RouterWorkingComponent;
  let fixture: ComponentFixture<RouterWorkingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ RouterWorkingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(RouterWorkingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
