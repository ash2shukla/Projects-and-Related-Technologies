import { TestBed, inject } from '@angular/core/testing';

import { SomeDependencyService } from './some-dependency.service';

describe('SomeDependencyService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [SomeDependencyService]
    });
  });

  it('should be created', inject([SomeDependencyService], (service: SomeDependencyService) => {
    expect(service).toBeTruthy();
  }));
});
