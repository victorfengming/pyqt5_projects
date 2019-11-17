---
layout: post
title: "Vue.js官方教程"
date: 2019-11-01 10:26:40
category: 'blog'
tags:
- Vue
- 笔记
---
* content
{:toc}


















# 序言 Vue.js介绍

## 概念

1. Vue.js:渐进式JavaScript框架  

2. 渐进式:可以由浅到深的由简单到复杂的方式使用Vue.js  



## 优点

1. 体积小  

    压缩后33k  

2. 更高的运行效率  

    基于虚拟dom  

3. 双向数据绑定  

    不用再去操作dom对象,把更多的精力投入到业务逻辑上  

4. 生态丰富、学习成本低  

    有大量成熟稳定的UI框架、常用组件  



## 使用场景

1. web端开发  

2. 移动端  

3. 跨平台应用开发  



# 第1节 安装与部署


## 使用<script>标签引入

1. 下载js文件并用`<script>`标签引入  

    - 开发版本:包含完整的警告和调试模式  

    - 生产版本:删除了警告,经过压缩更小  

2. CDN  

    - 最新版本(学习):`<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>`  

    - 生产环境:`<script src="https://cdn.jsdelivr.net/npm/vue@2.6.0"></script>`  

3. NPM  

    - 最新稳定版:`$ npm install vue`  



## 命令行工具(CLI)





# 第2节 创建第一个vue应用


## Vue.js 的核心

1. 是一个允许采用简洁的模板语法来声明式地将数据渲染进 DOM 的系统  



## 创建步骤  

1. html示例

    ```

    <div id="app">

        <!--用双大括号声明变量-->

        { { message } } 

    </div>

    ```



2. js示例

    ```

    <script type="text/javascript">

        //当引入Vue.js后会声明一个全局变量Vue

        //通过new Vue的方式会返回一个对象app,被称为应用对象

        //new Vue的时候需要传递一个对象做参数

        var app = new Vue({

            el: '#app', //元素,用id选择器选中app对应的div标签

            data: {

                message: 'Hello Vue!'

            }

        })

    </script>

    ```



## 创建应用的实质  

1. 每一个Vue应用都是通过`Vue()`函数创建一个`Vue实例`开始的  

2. 通常我们会使用一个变量接收Vue()函数被new的结果(对象)  

3. 虽然没有完全遵循`MVVM`模型，但是Vue的设计也受到了它的启发。因此在文档中经常会使用`vm(ViewModel)`这个变量名表示`Vue实例`  



# 第3节 数据与方法

## 数据与方法

1. 当一个Vue实例被创建时，它将`data`对象中的所有的属性加入到Vue的`响应式`系统中。当这些属性的值发生改变时，视图将会产生“响应”，即匹配更新为新的值。  

2. html示例

    ```

    <div id="app">

        <!--用双大括号声明变量-->

        { { a } } 

    </div>

    ```



3. js示例

    ```

    <script type="text/javascript">

        // 我们的数据对象

        var data = { a: 1 }

        

        // 该对象被加入到一个 Vue 实例中

        var vm = new Vue({

            // 如果我们想让某个属性或变量能够响应式,就要在new Vue()的时候提前声明

            el: "#app",

            data: data //前面的data是vm对象的属性,后面的data是用var定义的对象形式的全新的变量

        })

        

        // 获得这个实例上的属性

        // 返回源数据中对应的字段

        vm.a == data.a // => true

        

        // 设置属性也会影响到原始数据

        vm.a = 2

        data.a // => 2

        

        // ……反之亦然

        data.a = 3

        vm.a // => 3

    </script>

    ```



4. 如果你知道你会在晚些时候需要一个属性，但是一开始它为空或不存在，那么你仅需要设置一些初始值。  

5. 这里唯一的例外是使用`Object.freeze()`  ，这会阻止修改现有的属性，也意味着响应系统无法再追踪变化。  

6. 除了数据属性，Vue实例还暴露了一些有用的实例属性与方法。它们都有前缀`$`，以便与用户定义的属性区分开来。  

7. watch方法:可以观察一个变量的变化,并且为我们获取变化之前和变化之后的结果

    ```

    // 语法格式:Vue对象.$watch(要观察的变量,function(newVal,oldVal){})

    vm.$watch('a',function(newVal,oldVal){

        // 这个回调将在 `vm.a` 改变后调用

        console.log(newVal,oldVal);

    })

    ```



# 第4节 生命周期
## 生命周期钩子


1. 每个 Vue 实例在被创建时都要经过一系列的初始化过程——例如，需要设置数据监听、编译模板、将实例挂载到 DOM 并在数据变化时更新 DOM 等。同时在这个过程中也会运行一些叫做生命周期钩子的函数，这给了用户在不同阶段添加自己的代码的机会。  

2. 生命周期钩子需要些写在`new Vue()`的时候传递的这个对象内,以属性的方式进行声明。这个属性是个函数, 

Vue运行的这个应用运行的每个阶段,系统会自动调用这个已声明到的生命周期函数  

3. 声明周期函数不能使用箭头函数,`箭头函数`是没有`this`的,而this在生命周期过程中是要频繁应用的  

4. html示例



    ```

    <div id="app">

        <!--用双大括号声明变量-->

        { { msg } } 

    </div>

    ```



5. js示例

    ```

    // 该对象被加入到一个 Vue 实例中

    var vm = new Vue({

        el: "#app",

        data: {

            msg: "hi vue",

        },

        // 在实例初始化之后,数据观测(data observer)和watch/event事件配置之前被调用

        beforeCreate:function(){

            console.log('beforeCreate');

        },

            

        // 在实例化创建完成后被立即调用

        // 在这一步,实例已完成以下的配置:数据观测(data observer),属性和方法的运算,watch/event事件回调

        // 然而,挂载阶段还没开始,$el属性目前不可见

        created:function(){

            console.log('created');

        },

        

        // 在挂载开始之前被调用,相关的渲染函数首次被调用

        beforeMount:function(){

            console.log('beforeMount');

        },

        

        // el被新创建的vm.$el替换,挂载成功

        mounted:function(){

            console.log('mounted');

        },

        

        // 数据更新时调用

        beforeUpdate:function(){

            console.log('beforeUpdate');

        },

        

        // 组件DOM已经更新,组件更新完毕

        updated:function(){

            console.log('updated');

        },

    });



    // 定时器:3秒后把"hi Vue"改成"change..."

    setTimeout(function(){

        vm.msg = "change...";

    },3000);

    ```



# 第5节 模板语法-插值

## 文本

1. 数据绑定最常见的形式就是使用“Mustache”语法 (`双大括号`) 的文本插值：  

2. html示例

    ```

    <!-- 在整个页面上使用左右双大括号的方式去包裹一个变量,再在data里去声明属性及其取值 -->

    <span>Message: { { msg } }</span>

    ```



2. 通过使用`v-once`指令，你也能执行一次性地插值，当数据改变时，插值处的内容不会更新。但请留心这会影响到该节点上的其它数据绑定：  



3. html示例

    ```

    <!--这个标签不会改变:-->

    <div id="app" v-once>

        { { msg } } 

    </div>

    ```



4. js示例

    ```

    <script type="text/javascript">

        var vm = new Vue({

            el:"#app",

            data:{

                msg:"hi vue",

            }

        });

        vm.msg = "hi..." // 毫无作用

    </script>

    ```



## 原始HTML

1. 双大括号会将数据解释为普通文本，而非`HTML`代码。为了输出真正的`HTML`，你需要使用`v-html`指令：

2. html示例

    ```

    <div id="app">

        <p>Using mustaches: { { rawHtml } }</p>

        <p v-html="rawHtml"></p>

    </div>

    ```



3. js示例

    ```

    var vm = new Vue({

        el:"#app",

        data:{

            rawHtml:'<span style="color:red">this id should be red</span>'

        }

    });

    ```



## 特性

1. Mustache 语法不能作用在`HTML`特性上，遇到这种情况应该使用`v-bind`指令：  

2. html示例

    ```

    <div id="app">

        <div v-bind:class="color">test...</div>

    </div>

    ```



3. js示例

    ```

    var vm = new Vue({

        el:"#app",

        data:{

            color:'blue'

        }

    });

    ```



4. css示例

    ```

    .red{color:red;}

    .blue{color:blue;font-size: 100px;}

    ```



5. 语法格式:`v-bind:属性="某一变量的值"`  



## 使用JavaScript表达式

1. 迄今为止，在我们的模板中，我们一直都只绑定简单的属性键值。但实际上，对于所有的数据绑定，`Vue.js`都提供了完全的`JavaScript`表达式支持。  

2. html示例

    ```

    <div id="app">

        <!--表达式-->

        <p>{ { number + 1 } }</p>

        <!--三目运算:?前面可以是个表达式也可以是个变量,这个变量值是true或false-->

        <p>{ { ok ? 'YES' : 'NO' } }</p>

        <!--函数:核心变量是message,将Vue这个字符串以什么都没有为间隔拆分,返回一个数组,将这个数组反序,再连接成一个字符串-->

        <p>{ { message.split('').reverse().join('') } }</p>

    </div>

    ```



3. js示例

    ```

    var vm = new Vue({

        el:"#app",

        data:{

            number:10,

            ok:0,

            message:"Vue"

        }

    });

    ```



# 第6节 模板语法-指令

## 指令的概念

1. 指令 (Directives) 是带有`v-`前缀的特殊特性  

2. 指令特性的值预期是单个`JavaScript`表达式 (`v-for`是例外)  

3. 指令的职责是，当表达式的值改变时，将其产生的连带影响，响应式地作用于`DOM`。    

4. html示例

    ```

    <div id="app">

        <!--此处我们使用v-if进行条件渲染,p标签是否会被渲染取决于seen这个属性--> 

        <p v-if="seen">现在你看到我了</p>

    </div>

    ```



5. js示例

    ```

    var vm = new Vue({

        el:"#app",

        data:{

            seen:true

        }

    });

    ```



## 参数

1. 一些指令能够接收一个“参数”，在指令名称之后以`冒号`表示。  

2. `v-bind`指令可以用于响应式地更新 HTML 特性：  

3. html示例

    ```

    <div id="app">

        <!-- 在这里 href 是参数，告知 v-bind 指令将该元素的 href 特性与表达式 url 的值绑定。 -->

        <a v-bind:href="url">...</a>

    </div>

    ```



4. js示例

    ```

    var vm = new Vue({

        el:"#app",

        data:{

            url:"https://cn.vuejs.org/v2/guide/syntax.html"

        }

    });

    ```



2. v-on 指令，它用于监听 DOM 事件：

    ```

    <div id="app">

        <!-- 在这里参数是监听的事件名 -->

        <a v-on:click="doSomething">...</a>

    </div>

    ```



## 修饰符

1. 修饰符 (modifier) 是以半角句号`.`指明的特殊后缀，用于指出一个指令应该以特殊方式绑定。  

2. html示例

    ```

    <div id="app">

        <!--使用@click这样的指令可以为某一个元素绑定对应的事件-->

        <div @click="click1">

            <!--先执行click2,再执行click1-->

            <!--<div @click="click2">-->

            <!--.stop就是Vue的一个修饰符,当前的click2事件执行完毕后就停下来-->

            <div @click.stop="click2">

                click me

            </div>

        </div>

    </div>

    ```



3. js示例

    ```

    var vm = new Vue({

        el:"#app",

        data:{

            seen:false,

            url:"https://cn.vuejs.org/v2/guide/syntax.html"

        },

        methods:{ //在初始化Vue对象时使用methods这样的属性内部使用键值对的形式去声明方法和方法对应的函数体

            click1:function(){

                console.log('click1...');

            },

            click2:function(){

                console.log('click2...');

            }

        }

    });

    ```



# 第7节 class与style绑定

## 绑定HTML Class

1. 对象语法:我们可以传给`v-bind:class`一个对象，以动态地切换 class：

2. html示例

    ```

    <div id="app">

        <!--active属性是否能绑定到div标签里,取决于isActive的值-->

        <div v-bind:class="{ active:isActive }" style="width: 200px;height: 200px;text-align: center;line-height: 200px;">

            hi Vue

        </div>

    </div>

    ```



3. js示例

    ```

    var vm = new Vue({

        el:"#app",

        data:{

            isActive:true

        }

    });

    ```



4. css示例

    ```

    .active{background: #ff0000;}

    ```



5. html示例

    ```

    <!-- 你可以在对象中传入更多属性来动态切换多个 class。此外，v-bind:class 指令也可以与普通的 class 属性共存。 -->

    <div id="app">

        <!--active属性是否能绑定到div标签里,取决于isActive的值-->

        <div class="test" v-bind:class="{ active:isActive,green:isGreen }" style="width: 200px;height: 200px;text-align: center;line-height: 200px;">

            hi Vue

        </div>

    </div>

    ```



6. js示例

    ```

    var vm = new Vue({

        el:"#app",

        data:{

            isActive:true,

            isGreen:true

        }

    });

    ```



7. css示例

    ```

    .test{font-size: 30px;}

    .active{background: #ff0000;}

    .green{color:#00ff00;}

    ```



2. 数组语法:我们可以把一个数组传给`v-bind:class`，以应用一个 class 列表：

    ```

    <div id="app">

        <!--v-bind class语法还支持数组形式,里面用静态的方式添加样式-->

        <!--里面如果是动态的,支持通过三元运算的方式来为某一个具体的样式进行动态的赋值-->

        <div class="test" v-bind:class="[ isActive ? 'active' : '' , isGreen ? 'green' : '' ]" style="width: 200px;height: 200px;text-align: center;line-height: 200px;">

            hi Vue

        </div>

    </div>

    ```



## 绑定内联样式

1. 对象语法:`v-bind:style`的对象语法十分直观——看着非常像 CSS，但其实是一个 JavaScript 对象。CSS 属性名可以用驼峰式 (camelCase) 或短横线分隔 (kebab-case，记得用引号括起来) 来命名：

2. html示例

    ```

    <div id="app">

        <!--前面的color是style的属性,后面的color是变量-->

        <!--使用三元运算来进行样式的绑定-->

        <div :style="{color : color,fontSize:size,background:isRed ? '#ff0000':''}">

            hi Vue

        </div>  

    </div>

    ```



3. js示例

    ```

    var vm = new Vue({

        el:"#app",

        data:{

            color:'#00ff00',

            size:'50px',

            isRed:true

        }

    });

    ```



# 第8节 条件渲染

## v-if

1. `v-else-if`指令用于条件性地渲染一块内容。这块内容只会在指令的表达式返回 truthy 值的时候被渲染。  

2. html示例

    ```

    <div id="app">

        <div v-if="type === 'A'">

            A

        </div>

        <div v-else-if="type === 'B'">

            B

        </div>

        <div v-else-if="type === 'C'">

            C

        </div>

        <div v-else>

            Not A/B/C

        </div>

    </div>

    ```



3. js示例

    ```

    var vm = new Vue({

        el:"#app",

        data:{

            type:""

        }

    });

    ```



## v-show

1. 用于根据条件展示元素的选项是`v-show`指令。  

2. html示例

    ```

    <div id="app">

        <!--不同的是带有 v-show 的元素始终会被渲染并保留在 DOM 中。v-show 只是简单地切换元素的 CSS 属性 display。-->

        <h1 v-show="ok">hello</h1>

    </div>

    ```



3. js示例

    ```

    var vm = new Vue({

        el:"#app",

        data:{

            ok:false //通过控制台可以看到h1标签内容,只是页面不显示display:none

        }

    });

    ```



## v-if vs v-show

1. v-if 是“真正”的条件渲染，因为它会确保在切换过程中条件块内的事件监听器和子组件适当地被销毁和重建。



2. v-if 也是惰性的：如果在初始渲染时条件为假，则什么也不做——直到条件第一次变为真时，才会开始渲染条件块。



3. 相比之下，v-show 就简单得多——不管初始条件是什么，元素总是会被渲染，并且只是简单地基于 CSS 进行切换。



4. 一般来说，v-if 有更高的切换开销，而 v-show 有更高的初始渲染开销。因此，如果需要非常频繁地切换，则使用 v-show 较好；如果在运行时条件很少改变，则使用 v-if 较好。



# 第9节 列表渲染

## 用 v-for 把一个数组对应为一组元素

1. 我们可以用`v-for`指令基于一个数组来渲染一个列表。v-for 指令需要使用`item in items`形式的特殊语法，其中`items`是源数据数组，而`item`则是被迭代的数组元素的别名。  

2. html示例

    ```

    <ul id="example-1">

        <li v-for="item in items">

            { { item.message } }

        </li>

    </ul>

    ```



3. js示例

    ```

    var example1 = new Vue({

        el: '#example-1',

        data: {

            items: [

                { message: 'Foo' },

                { message: 'Bar' }

            ]

        }

    })

    ```



4. 在`v-for`块中，我们可以访问所有父作用域的属性。v-for 还支持一个可选的第二个参数，即当前项的索引。  

5. html示例

    ```

    <ul id="example-2">

        <li v-for="(item, index) in items">

            { { parentMessage } } - { { index } } - { { item.message } }

        </li>

    </ul>

    ```



6. js示例

    ```

    var example2 = new Vue({

        el: '#example-2',

        data: {

            parentMessage: 'Parent',

            items: [{

                message: 'Foo'

            }, {

                message: 'Bar'

            },]

        }

    })

    ```



## 在 v-for 里使用对象

1. 你也可以用 v-for 来遍历一个对象的属性。  

2. html示例

    ```

    <ul id="v-for-object" class="demo">

        <li v-for="value, key in object">

            { { key } } : { { value } }

        </li>

    </ul>

    ```



3. js示例

    ```

    new Vue({

        el: '#v-for-object',

        data: {

            object: {

                title: 'How to do lists in Vue',

                author: 'Jane Doe',

                publishedAt: '2016-04-10'

            }

        }

    })

    ```



## 维护状态

1. 当`Vue`正在更新使用`v-for`渲染的元素列表时，它默认使用“`就地更新`”的策略。如果数据项的顺序被改变，`Vue`将不会移动`DOM`元素来匹配数据项的顺序，而是就地更新每个元素，并且确保它们在每个索引位置正确渲染。



2. 这个默认的模式是高效的，但是只适用于不依赖子组件状态或临时 DOM 状态 (例如：表单输入值) 的列表渲染输出。



3. 为了给 Vue 一个提示，以便它能跟踪每个节点的身份，从而重用和重新排序现有元素，你需要为每项提供一个唯一 key 属性：

    ```

    <ul id="v-for-object">

        <!--:key等同于v-bind:key-->

        <li v-for="value, index in object" :key="index">

            { { index } } : { { value } }

        </li>

    </ul>

    ```



# 第10节 事件绑定

## 监听事件

1. 可以用`v-on`指令监听`DOM`事件，并在触发时运行一些`JavaScript`代码。  

2. html示例

    ```

    <div id="example-1">

        <button v-on:click="counter += 1">Add { { counter } } </button>

    </div>

    ```



3. js示例

    ```

    var example1 = new Vue({

        el: '#example-1',

        data: {

            counter: 0

        }

    })

    ```



## 事件处理方法

1. 然而许多事件处理逻辑会更为复杂，所以直接把 JavaScript 代码写在 v-on 指令中是不可行的。因此 v-on 还可以接收一个需要调用的方法名称。  

2. html示例

    ```

    <div id="example-2">

        <!-- `greet` 是在下面定义的方法名 -->

        <!--有时也需要在内联语句处理器中访问原始的 DOM 事件。可以用特殊变量 $event 把它传入方法-->

        <button v-on:click="greet('abc',$event)">Greet</button>

    </div>

    ```



3. js示例

    ```

    var example2 = new Vue({

        el: '#example-2',

        data: {

            name: 'caoyang'

        },

        // 在 `methods` 对象中定义方法

        methods: {

            greet: function(str,e) {

                // `this` 在方法里指向当前 Vue 实例

                alert('Hello ' + this.name + '!')

                // `event` 是原生 DOM 事件

                if(event) {

                    alert(e.target.tagName)

                    console.log(e)

                }

            }

        }

    })



    // 也可以用 JavaScript 直接调用方法

    example2.greet() // => 'Hello caoyang!'

    ```



## 事件修饰符



1. 在事件处理程序中调用 event.preventDefault() 或 event.stopPropagation() 是非常常见的需求。尽管我们可以在方法中轻松实现这点，但更好的方式是：方法只有纯粹的数据逻辑，而不是去处理 DOM 事件细节。



2. 为了解决这个问题，`Vue.js`为`v-on`提供了事件修饰符。之前提过，修饰符是由点开头的指令后缀来表示的。  



    ```

    <!-- 阻止单击事件继续传播 -->

    <a v-on:click.stop="doThis"></a>



    <!-- 提交事件不再重载页面 -->

    <form v-on:submit.prevent="onSubmit"></form>



    <!-- 修饰符可以串联 -->

    <a v-on:click.stop.prevent="doThat"></a>



    <!-- 只有修饰符 -->

    <form v-on:submit.prevent></form>



    <!-- 添加事件监听器时使用事件捕获模式 -->

    <!-- 即内部元素触发的事件先在此处理，然后才交由内部元素进行处理 -->

    <div v-on:click.capture="doThis">...</div>



    <!-- 只当在 event.target 是当前元素自身时触发处理函数 -->

    <!-- 即事件不是从内部元素触发的 -->

    <div v-on:click.self="doThat">...</div>

    ```



3. `v-on`指令可以绑定html元素拥有的所有的事件



# 第11节 表单输入绑定

## 基础用法

1. 你可以用`v-model`指令在表单`<input>`、`<textarea>`及`<select>`元素上创建双向数据绑定。它会根据控件类型自动选取正确的方法来更新元素。  

2. `v-model`本质上不过是语法糖。它负责监听用户的输入事件以更新数据，并对一些极端场景进行一些特殊处理。  

3. v-model 在内部为不同的输入元素使用不同的属性并抛出不同的事件：

    - text 和 textarea 元素使用 value 属性和 input 事件；

    - checkbox 和 radio 使用 checked 属性和 change 事件；

    - select 字段将 value 作为 prop 并将 change 作为事件。  

4. html示例

    ```

    <div id="app">

        <input v-model="message" placeholder="edit me">

        <p>input: { { message } }</p>



        <textarea v-model="message2" placeholder="add multiple lines"></textarea>

        <p style="white-space: pre-line;">textarea: { { message2 } }</p>



        <input type="checkbox" id="checkbox" v-model="checked">

        <label for="checkbox">{ { checked } }</label>

        <br>



        <input type="checkbox" id="jack" value="Jack" v-model="checkedNames">

        <label for="jack">Jack</label>

        <input type="checkbox" id="john" value="John" v-model="checkedNames">

        <label for="john">John</label>

        <input type="checkbox" id="mike" value="Mike" v-model="checkedNames">

        <label for="mike">Mike</label>

        <br>

        <span>Checked names: { { checkedNames } }</span>

        <br>



        <input type="radio" id="one" value="One" v-model="picked">

        <label for="one">One</label>

        <input type="radio" id="two" value="Two" v-model="picked">

        <label for="two">Two</label>

        <br>

        <span>Picked: { { picked } }</span>

        <br>



        <select v-model="selected">

            <option disabled value="">请选择</option>

            <option>A</option>

            <option>B</option>

            <option>C</option>

        </select>

        <br>

        <span>Selected: { { selected } }</span>

    </div>

    ```



5. js示例

    ```

    var vm = new Vue({

        el: '#app',

        data: {

            message: "",

            message2: "",

            checked: true,

            checkedNames: [],

            picked: '',

            selected: ''

        }

    })

    ```



## 值绑定

1. 对于单选按钮，复选框及选择框的选项，v-model 绑定的值通常是静态字符串 (对于复选框也可以是布尔值)：

    ```

    <!-- 当选中时，`picked` 为字符串 "a" -->

    <input type="radio" v-model="picked" value="a">



    <!-- `toggle` 为 true 或 false -->

    <input type="checkbox" v-model="toggle">



    <!-- 当选中第一个选项时，`selected` 为字符串 "abc" -->

    <select v-model="selected">

        <option value="abc">ABC</option>

    </select>

    ```



2. 复选框:

    ```

    <input

        type="checkbox"

        v-model="toggle"

        true-value="yes"

        false-value="no"

    >



    // 当选中时

    vm.toggle === 'yes'

    // 当没有选中时

    vm.toggle === 'no'

    ```



3. 单选按钮

    ```

    <input type="radio" v-model="pick" v-bind:value="a">



    // 当选中时

    vm.pick === vm.a

    ```



4. 选择框的选项

    ```

    <select v-model="selected">

        <!-- 内联对象字面量 -->

        <option v-bind:value="{ number: 123 }">123</option>

    </select>



    // 当选中时

    typeof vm.selected // => 'object'

    vm.selected.number // => 123

    ```



## 表单提交

1. 在html文件中加一个提交按钮

    ```

    <button type="button" @click="submit">提交</button>



    methods:{

        submit:function(){

            console.log(this.message); //只打印出单行文本的内容

            // 声明一个对象形式的变量,将表单所有的值收集起来

            var postObj = {

                msg1:this.message,

                msg2:this.message2,

                checkval:this.checkedNames

            }

            console.log(postObj);

        }

    }

    ```



# 第12节 组件基础

## 基本示例

1. 组件是可复用的 Vue 实例，把经常重复的功能封装成组件,达到快捷开发的目的  

2. 创建组件语法格式:`Vue.component(组件名称,{以对象的形式描述组件})`  

3. 因为组件是可复用的 Vue 实例，所以它们与 new Vue 接收相同的选项  

4. 示例

    ```

    <div id="components-demo">

        <!--采用html标签的形式对组件进行调用,标签的名称就是组件的名称-->

        <button-counter title="title1;"></button-counter>

        <!--组件是可以复用的-->

        <button-counter title="title2;"></button-counter>

    </div>





    <script type="text/javascript">

        // 定义一个名为 button-counter 的新组件

        Vue.component('button-counter', {

            // 通过props为组件定义属性

            props:['title'],

            data: function() {

                return {

                    count: 0

                }

            },

            // 创建一个模板时需注意,一个组件的模板必须具备一个根节点

            template: '<div><h1>h1...</h1><button v-on:click="count++">{ {title} } You clicked me { { count } } times.</button></div>'

        })

        

        var vm = new Vue({

            el:"#components-demo",

            data:{  

            }

        });

    </script>

    ```



## 监听子组件事件

1. 示例

    ```

    <div id="components-demo">

        <!--5. 在组件的父级可以通过事件绑定的方式去接收到emit函数所触发的事件-->

        <button-counter title="title1;" @clicknow="clicknow">

            <!--8. 在组件的标签内部可以插入一些自定义的html内容-->

            <h2>h2...</h2>

        </button-counter>

    </div>



    <script type="text/javascript">

        Vue.component('button-counter', {

            props:['title'],

            data: function() {

                return {

                    count: 0

                }

            },

            

            // 7. 在模板内我们可以通过slot标签声明一个组件的插槽,通过插槽可以插入任意的html内容及标签 

            // 1. 把click++改成一个可执行的JavaScript函数 

            template: '<div><h1>h1...</h1><button v-on:click="clickfun">{ {title} } You clicked me { { count } } times.</button><slot></slot></div>',

            // 2. 使用methods属性去声明对应的函数

            methods:{

                clickfun:function(){

                    // 3. 在函数内部使用this对象对click变量进行处理,点击button按钮,count由0变成1

                    this.count++;

                    // 4. 使用this对象的emit方法去触发一个事件

                    // 语法格式::this.$emit(事件名称,可携带的一些参数);

                    this.$emit('clicknow',this.count);

                }

            }

        })

        

        var vm = new Vue({

            el:"#components-demo",

            data:{  

            },

            // 在页面上使用methods属性去声明clicknow方法

            methods:{

                // 6. 函数能够正确执行,并可以接收组件内部传递出来的count数据的值 

                clicknow:function(e){

                    console.log(e);

                }

            }

        });

    </script>

    ```





# 第13节 组件注册





# 第14节 单文件组件

# 第15节 免终端开发vue应用





















