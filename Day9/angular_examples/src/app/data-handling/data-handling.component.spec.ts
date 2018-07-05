import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { DataHandlingComponent } from './data-handling.component';

describe('DataHandlingComponent', () => {
  let component: DataHandlingComponent;
  let fixture: ComponentFixture<DataHandlingComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ DataHandlingComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(DataHandlingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
