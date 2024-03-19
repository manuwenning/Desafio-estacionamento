import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module'; // Importe o AppRoutingModule
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { CadastroComponent } from './cadastro/cadastro.component';
import { OperacaoComponent } from './operacao/operacao.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    CadastroComponent,
    OperacaoComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule // Certifique-se de importar o AppRoutingModule aqui
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }







