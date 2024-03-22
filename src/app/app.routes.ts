import { ModuleWithProviders } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './home/home.component';
import { CadastroComponent } from './cadastro/cadastro.component';
import { OperacaoComponent } from './operacao/operacao.component';

const routes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'cadastro', component: CadastroComponent },
  { path: 'operacao', component: OperacaoComponent },
];

export const AppRoutingModule: ModuleWithProviders<RouterModule> = RouterModule.forRoot(routes);


