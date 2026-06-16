# 常见交互模式（Alpine.js 速查）

> 用于 Step 4。直接复制粘贴的常见交互代码。

## 1. 页面跳转（哈希路由）

```html
<!-- 链接：用 a 标签 hash 跳转 -->
<a href="#/list" class="text-primary">查看全部</a>

<!-- 路由器（写在 index.html 里） -->
<div x-data="router()" x-init="init()">
  <iframe :src="currentPage" class="w-full h-screen border-0"></iframe>
</div>
<script>
function router() {
  return {
    currentPage: 'pages/home.html',
    routes: {
      '#/':       'pages/home.html',
      '#/list':   'pages/list.html',
      '#/detail': 'pages/detail.html',
    },
    init() {
      const route = () => {
        this.currentPage = this.routes[location.hash] || this.routes['#/']
      }
      route()
      window.addEventListener('hashchange', route)
    }
  }
}
</script>
```

## 2. Tab 切换

```html
<div x-data="{ active: 'all' }">
  <div class="flex border-b">
    <button :class="active==='all' ? 'border-primary text-primary border-b-2' : 'text-text-2'"
            @click="active='all'" class="px-4 py-2">全部</button>
    <button :class="active==='done' ? 'border-primary text-primary border-b-2' : 'text-text-2'"
            @click="active='done'" class="px-4 py-2">已完成</button>
  </div>
  <div x-show="active==='all'">全部内容...</div>
  <div x-show="active==='done'">已完成内容...</div>
</div>
```

## 3. 模态弹窗 (Modal)

```html
<div x-data="{ open: false }">
  <button @click="open = true" class="px-4 py-2 bg-primary text-white rounded-md">
    打开弹窗
  </button>

  <!-- 遮罩 -->
  <div x-show="open" x-transition.opacity
       @click="open = false"
       class="fixed inset-0 bg-black/50 z-40"></div>

  <!-- 弹窗体 -->
  <div x-show="open"
       x-transition:enter="transition ease-out duration-200"
       x-transition:enter-start="opacity-0 scale-95"
       x-transition:enter-end="opacity-100 scale-100"
       class="fixed inset-0 flex items-center justify-center z-50 pointer-events-none">
    <div class="bg-white rounded-lg shadow-dialog p-6 w-96 pointer-events-auto">
      <h3 class="text-lg font-semibold">确认操作</h3>
      <p class="text-text-2 mt-2">确定要删除这条记录吗？</p>
      <div class="mt-4 flex justify-end gap-2">
        <button @click="open=false" class="px-4 py-2 text-text-2">取消</button>
        <button @click="open=false" class="px-4 py-2 bg-red-500 text-white rounded">删除</button>
      </div>
    </div>
  </div>
</div>
```

## 4. 抽屉 (Drawer)

```html
<div x-data="{ open: false }">
  <button @click="open=true">打开</button>

  <!-- 遮罩 -->
  <div x-show="open" x-transition.opacity @click="open=false"
       class="fixed inset-0 bg-black/40 z-40"></div>

  <!-- 抽屉体（右侧划入）-->
  <div x-show="open"
       x-transition:enter="transition ease-out duration-300"
       x-transition:enter-start="translate-x-full"
       x-transition:enter-end="translate-x-0"
       x-transition:leave="transition ease-in duration-200"
       x-transition:leave-start="translate-x-0"
       x-transition:leave-end="translate-x-full"
       class="fixed right-0 top-0 h-full w-80 bg-white shadow-dialog z-50 p-6">
    抽屉内容
  </div>
</div>
```

## 5. Toast 提示

```html
<div x-data="toast()" x-init="init()">
  <button @click="show('保存成功', 'success')">触发</button>

  <div x-show="visible"
       x-transition
       :class="type==='success' ? 'bg-green-500' : 'bg-red-500'"
       class="fixed top-6 left-1/2 -translate-x-1/2 px-4 py-2 text-white rounded-md shadow-card z-50">
    <span x-text="msg"></span>
  </div>
</div>
<script>
function toast() {
  return {
    visible: false, msg: '', type: 'success',
    show(msg, type='success') {
      this.msg = msg; this.type = type; this.visible = true;
      setTimeout(() => this.visible = false, 2500)
    },
    init() { window.toast = this }  // 全局调用 window.toast.show(...)
  }
}
</script>
```

## 6. 表单 + 校验

```html
<form x-data="{ name:'', email:'', errors:{} }"
      @submit.prevent="
        errors = {};
        if (!name) errors.name = '请输入姓名';
        if (!email.includes('@')) errors.email = '邮箱格式错误';
        if (Object.keys(errors).length === 0) {
          window.toast.show('提交成功');
        }
      "
      class="space-y-4">
  <div>
    <label class="block text-sm text-text-2">姓名</label>
    <input x-model="name"
           class="mt-1 w-full px-3 py-2 border rounded-md focus:border-primary focus:outline-none">
    <p x-show="errors.name" x-text="errors.name" class="text-red-500 text-xs mt-1"></p>
  </div>
  <div>
    <label class="block text-sm text-text-2">邮箱</label>
    <input x-model="email" type="email"
           class="mt-1 w-full px-3 py-2 border rounded-md focus:border-primary focus:outline-none">
    <p x-show="errors.email" x-text="errors.email" class="text-red-500 text-xs mt-1"></p>
  </div>
  <button type="submit" class="px-4 py-2 bg-primary text-white rounded-md">提交</button>
</form>
```

## 7. 加载/空/错误三态

```html
<div x-data="{ state:'loading', items:[] }"
     x-init="
       setTimeout(() => {
         state = 'success';
         items = [{id:1, name:'示例 1'}, {id:2, name:'示例 2'}];
         // state = 'empty'  // 测试空态
         // state = 'error'  // 测试错误态
       }, 1000)">

  <!-- 加载中：Skeleton -->
  <template x-if="state==='loading'">
    <div class="space-y-3">
      <template x-for="i in 3">
        <div class="h-16 bg-bg-2 rounded animate-pulse"></div>
      </template>
    </div>
  </template>

  <!-- 空态 -->
  <template x-if="state==='empty'">
    <div class="text-center py-12 text-text-3">
      <div class="text-5xl mb-2">📭</div>
      <p>暂无数据</p>
      <button class="mt-4 px-4 py-2 bg-primary text-white rounded">立即创建</button>
    </div>
  </template>

  <!-- 错误态 -->
  <template x-if="state==='error'">
    <div class="text-center py-12">
      <p class="text-red-500">加载失败</p>
      <button @click="state='loading'" class="mt-2 text-primary">重试</button>
    </div>
  </template>

  <!-- 成功态 -->
  <template x-if="state==='success'">
    <div class="space-y-2">
      <template x-for="item in items" :key="item.id">
        <div class="p-4 bg-white rounded-md shadow-card" x-text="item.name"></div>
      </template>
    </div>
  </template>
</div>
```

## 8. 下拉菜单 (Dropdown)

```html
<div x-data="{ open: false }" @click.outside="open=false" class="relative">
  <button @click="open=!open" class="px-3 py-2 border rounded-md">
    操作 <span class="ml-1">▾</span>
  </button>
  <div x-show="open" x-transition
       class="absolute right-0 mt-1 w-40 bg-white shadow-card rounded-md py-1 z-10">
    <a href="#" class="block px-4 py-2 hover:bg-bg-2">编辑</a>
    <a href="#" class="block px-4 py-2 hover:bg-bg-2">复制</a>
    <a href="#" class="block px-4 py-2 hover:bg-bg-2 text-red-500">删除</a>
  </div>
</div>
```

## 9. 分页

```html
<div x-data="{ page:1, total:10 }" class="flex items-center gap-2">
  <button @click="page>1 && page--" :disabled="page===1"
          class="px-3 py-1 border rounded disabled:opacity-30">上一页</button>
  <span x-text="`${page} / ${total}`" class="px-3"></span>
  <button @click="page<total && page++" :disabled="page===total"
          class="px-3 py-1 border rounded disabled:opacity-30">下一页</button>
</div>
```

## 10. 移动端底部 Tab 栏

```html
<nav class="fixed bottom-0 left-0 right-0 bg-white border-t flex">
  <a href="#/" class="flex-1 py-3 text-center" :class="$store.tab==='home' ? 'text-primary' : 'text-text-3'">
    <div class="text-xl">🏠</div>
    <div class="text-xs">首页</div>
  </a>
  <a href="#/list" class="flex-1 py-3 text-center" :class="$store.tab==='list' ? 'text-primary' : 'text-text-3'">
    <div class="text-xl">📋</div>
    <div class="text-xs">列表</div>
  </a>
  <a href="#/me" class="flex-1 py-3 text-center" :class="$store.tab==='me' ? 'text-primary' : 'text-text-3'">
    <div class="text-xl">👤</div>
    <div class="text-xs">我的</div>
  </a>
</nav>
```

## 使用建议

- **优先用现成的**：复制本文件代码块，改文案/Token 即可
- **不要追求 100% 还原**：原型阶段 80% 还原已足够
- **保持一致**：同一交互在不同页面用同一种实现
