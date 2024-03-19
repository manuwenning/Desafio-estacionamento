import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OperacaoComponent } from './operacao.component';

describe('OperacaoComponent', () => {
  let component: OperacaoComponent;
  let fixture: ComponentFixture<OperacaoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [OperacaoComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(OperacaoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
