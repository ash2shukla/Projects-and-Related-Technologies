import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { RouterModule, Routes } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { DataHandlingComponent } from './data-handling/data-handling.component';
import { LifecycleComponent } from './lifecycle/lifecycle.component';
import { FormHandlingComponent } from './form-handling/form-handling.component';
import { DepInjectComponent } from './dep-inject/dep-inject.component';
import { ObservablesExComponent } from './observables-ex/observables-ex.component';
import { HttpInteractComponent } from './http-interact/http-interact.component';

import { SomeDependencyService } from './some-dependency.service';
import { WebsocketComponent } from './websocket/websocket.component';
import { RouterWorkingComponent } from './router-working/router-working.component';

// const appRoutes: Routes = [
//   { path: 'exdata', component: DataHandlingComponent },
//   { path: 'exlifec', component: LifecycleComponent },
//   { path: 'exdepin', component: DepInjectComponent },
//   // { path: 'ex',
//   //   redirectTo: '/exdata',
//   //   pathMatch: 'full'
//   // },
//   { path: '**', component: AppComponent } // <-- In no path matched
// ];

@NgModule({
  declarations: [
    AppComponent,
    DataHandlingComponent,
    LifecycleComponent,
    FormHandlingComponent,
    DepInjectComponent,
    ObservablesExComponent,
    HttpInteractComponent,
    WebsocketComponent,
    RouterWorkingComponent,
  ],
  imports: [
    RouterModule.forRoot(
      [],
      { enableTracing: true } // <-- debugging purposes only
    ),
    BrowserModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
  ],
  providers: [SomeDependencyService],
  bootstrap: [AppComponent]
})
export class AppModule { }
