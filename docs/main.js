(window["webpackJsonp"] = window["webpackJsonp"] || []).push([["main"],{

/***/ "./src/$$_lazy_route_resource lazy recursive":
/*!**********************************************************!*\
  !*** ./src/$$_lazy_route_resource lazy namespace object ***!
  \**********************************************************/
/*! no static exports found */
/***/ (function(module, exports) {

function webpackEmptyAsyncContext(req) {
	// Here Promise.resolve().then() is used instead of new Promise() to prevent
	// uncaught exception popping up in devtools
	return Promise.resolve().then(function() {
		var e = new Error("Cannot find module '" + req + "'");
		e.code = 'MODULE_NOT_FOUND';
		throw e;
	});
}
webpackEmptyAsyncContext.keys = function() { return []; };
webpackEmptyAsyncContext.resolve = webpackEmptyAsyncContext;
module.exports = webpackEmptyAsyncContext;
webpackEmptyAsyncContext.id = "./src/$$_lazy_route_resource lazy recursive";

/***/ }),

/***/ "./src/app/app.component.css":
/*!***********************************!*\
  !*** ./src/app/app.component.css ***!
  \***********************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = ".container {}\r\n\r\n#left-panel {\r\n  margin-top: 5%;\r\n}\r\n\r\n#right-panel {\r\n  margin-top: 5%;\r\n}\r\n\r\n.video {\r\n  margin-left: 5%;\r\n}\r\n\r\n.github-btn {\r\n  border: darkred;\r\n  background-color: darkred;\r\n  color: white;\r\n  box-shadow: 5px 4px 8px rgba(0, 0, 0, 0.5);\r\n  padding: 9px;\r\n  border-radius: 7px;\r\n}\r\n\r\n.github-btn a {\r\n    color: white;\r\n}\r\n\r\npre.code-snippet {\r\n  width: 90%;\r\n  height: 25;\r\n  border: 2px solid black;\r\n  overflow: scroll;\r\n  background-color: lightgrey;\r\n}\r\n\r\np#whatis-text {\r\n    font-size: 150%;\r\n}\r\n\r\n.section-title {\r\n    color: darkred;\r\n}\r\n\r\n.instructions {\r\n    font-size: 125%;\r\n}\r\n"

/***/ }),

/***/ "./src/app/app.component.html":
/*!************************************!*\
  !*** ./src/app/app.component.html ***!
  \************************************/
/*! no static exports found */
/***/ (function(module, exports) {

module.exports = "<div class=\"container\">\n\n  <div class=\"row\">\n\n    <div class=\"col s4\" id=\"left-panel\">\n      <h3>NatAlert</h3>\n      <p>Programming Language for the development of Notification applications</p>\n\n      <a class=\"github-btn\" href=\"https://github.com/CSantiagoBerio/NatAlert\">View in Github</a>\n    </div>\n\n    <div class=\"col s8\" id=\"right-panel\">\n      <h4>Tutorial:</h4>\n      <iframe class=\"video\" width=\"400\" height=\"250\" src=\"https://www.youtube.com/embed/Jb6YbvuhUgQ\" frameborder=\"0\"\n        allow=\"accelerometer; encrypted-media; gyroscope; picture-in-picture\" allowfullscreen></iframe>\n\n      <h4 class=\"section-title\">What is NatAlert?</h4>\n      <p id=\"whatis-text\">NatAlert is a simple to use and has a non-difficult learning curve. It was developed for the\n        purpose of\n        attracting developers and non-developers, as it does not require any programming background. All it needs to\n        function is NatAlert own language syntax, which is easy to learn. Non-developer do not need to know how to\n        develop a GUI or how to connect the GUI components to a specified function or method, all of this is made in\n        the background by NatAlert.</p>\n      <h4 class=\"section-title\">Code Syntax:</h4>\n      <pre class=\"code-snippet\">\n          <code>\n          DB.INIT();\n\n          UI.NEW {{ '{' }}\n            TITLE: \"EVENT\";\n            EVENTS: \"Fire\", \"Power Outage\", \"Elevator broke down\";\n            LOCATIONS: \"Finance Department\", \"IT Department\", \"Laboratory Bldg.\";\n            SENDTO: \"Finance Department Personnel\", \"IT Personnel\", \"Researchers\";\n            {{ '}' }}\n\n          UI.INIT();\n          </code>\n      </pre>\n\n      <h4 class=\"section-title\">Instructions:</h4>\n      <p class=\"instructions\">\n        <span class=\"section-title\">Python 3.6: </span> <br> For the installation of python 3.6 or higher go to python.org and install the latest update.\n        <br>\n        <span class=\"section-title\"> Pip: </span> <br> Pip is a tool used for installing python dependencies, if you are installing python 3.6 or higher pip\n        comes already installed in your system. <br>\n        <span class=\"section-title\"> PyQT5: </span> <br> For installing pyqt5 you just need to go to the terminal and proceed with the following command to\n        install the dependencies to the system. <br>\n\n        <span class=\"section-title\"> PyreBase: </span> <br> Pyrebase is the library used to communicate with the firebase database used in this language. To\n        be\n        able to install this dependency go to the terminal and proceed with the following command to install the\n        dependency to the system. <br>\n\n        <span class=\"section-title\"> Ply:  </span><br> For installing the parser for our language go to GitHub and clone the repository for ply.py and\n        yax.py and\n        include them inside your environment. <br>\n\n        <span class=\"section-title\"> NatAlert: </span><br> For the use of our language go to the NatAlert repository and clone the project to be able to\n        use it on your system. <br>\n\n        <span class=\"section-title\"> Usage: </span> <br>\n        <span class=\"section-title\"> Writing/Running Code: </span> <br> For the process of writing code open the existing input.txt file available inside the\n        NatAlert repo just downloaded. On that txt file you will find a code example. Proceed to write the necessary\n        code for the purpose of alerting of a specific emergency. After finishing and saving the txt file proceed to\n        run the natparse.py for the system to start reading your recently created code and proceed to make use of you\n        new GUI. For additional changes the user can create multiple txt files but ensure that they are all labeled as\n        input.txt before use inside NatAlert.\n      </p>\n\n    </div>\n\n  </div>\n\n\n</div>\n"

/***/ }),

/***/ "./src/app/app.component.ts":
/*!**********************************!*\
  !*** ./src/app/app.component.ts ***!
  \**********************************/
/*! exports provided: AppComponent */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppComponent", function() { return AppComponent; });
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};

var AppComponent = /** @class */ (function () {
    function AppComponent() {
        this.title = 'NatAlert';
    }
    AppComponent = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["Component"])({
            selector: 'app-root',
            template: __webpack_require__(/*! ./app.component.html */ "./src/app/app.component.html"),
            styles: [__webpack_require__(/*! ./app.component.css */ "./src/app/app.component.css")]
        })
    ], AppComponent);
    return AppComponent;
}());



/***/ }),

/***/ "./src/app/app.module.ts":
/*!*******************************!*\
  !*** ./src/app/app.module.ts ***!
  \*******************************/
/*! exports provided: AppModule */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "AppModule", function() { return AppModule; });
/* harmony import */ var _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/platform-browser */ "./node_modules/@angular/platform-browser/fesm5/platform-browser.js");
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _app_component__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./app.component */ "./src/app/app.component.ts");
var __decorate = (undefined && undefined.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};



var AppModule = /** @class */ (function () {
    function AppModule() {
    }
    AppModule = __decorate([
        Object(_angular_core__WEBPACK_IMPORTED_MODULE_1__["NgModule"])({
            declarations: [
                _app_component__WEBPACK_IMPORTED_MODULE_2__["AppComponent"]
            ],
            imports: [
                _angular_platform_browser__WEBPACK_IMPORTED_MODULE_0__["BrowserModule"]
            ],
            providers: [],
            bootstrap: [_app_component__WEBPACK_IMPORTED_MODULE_2__["AppComponent"]]
        })
    ], AppModule);
    return AppModule;
}());



/***/ }),

/***/ "./src/environments/environment.ts":
/*!*****************************************!*\
  !*** ./src/environments/environment.ts ***!
  \*****************************************/
/*! exports provided: environment */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony export (binding) */ __webpack_require__.d(__webpack_exports__, "environment", function() { return environment; });
// This file can be replaced during build by using the `fileReplacements` array.
// `ng build --prod` replaces `environment.ts` with `environment.prod.ts`.
// The list of file replacements can be found in `angular.json`.
var environment = {
    production: false
};
/*
 * For easier debugging in development mode, you can import the following file
 * to ignore zone related error stack frames such as `zone.run`, `zoneDelegate.invokeTask`.
 *
 * This import should be commented out in production mode because it will have a negative impact
 * on performance if an error is thrown.
 */
// import 'zone.js/dist/zone-error';  // Included with Angular CLI.


/***/ }),

/***/ "./src/main.ts":
/*!*********************!*\
  !*** ./src/main.ts ***!
  \*********************/
/*! no exports provided */
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
__webpack_require__.r(__webpack_exports__);
/* harmony import */ var _angular_core__WEBPACK_IMPORTED_MODULE_0__ = __webpack_require__(/*! @angular/core */ "./node_modules/@angular/core/fesm5/core.js");
/* harmony import */ var _angular_platform_browser_dynamic__WEBPACK_IMPORTED_MODULE_1__ = __webpack_require__(/*! @angular/platform-browser-dynamic */ "./node_modules/@angular/platform-browser-dynamic/fesm5/platform-browser-dynamic.js");
/* harmony import */ var _app_app_module__WEBPACK_IMPORTED_MODULE_2__ = __webpack_require__(/*! ./app/app.module */ "./src/app/app.module.ts");
/* harmony import */ var _environments_environment__WEBPACK_IMPORTED_MODULE_3__ = __webpack_require__(/*! ./environments/environment */ "./src/environments/environment.ts");




if (_environments_environment__WEBPACK_IMPORTED_MODULE_3__["environment"].production) {
    Object(_angular_core__WEBPACK_IMPORTED_MODULE_0__["enableProdMode"])();
}
Object(_angular_platform_browser_dynamic__WEBPACK_IMPORTED_MODULE_1__["platformBrowserDynamic"])().bootstrapModule(_app_app_module__WEBPACK_IMPORTED_MODULE_2__["AppModule"])
    .catch(function (err) { return console.error(err); });


/***/ }),

/***/ 0:
/*!***************************!*\
  !*** multi ./src/main.ts ***!
  \***************************/
/*! no static exports found */
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__(/*! C:\Users\csant\Desktop\NatAlert\src\main.ts */"./src/main.ts");


/***/ })

},[[0,"runtime","vendor"]]]);
//# sourceMappingURL=main.js.map