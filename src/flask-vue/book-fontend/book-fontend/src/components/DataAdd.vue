<script setup>
import axios from 'axios';
import { ElMessageBox } from 'element-plus';
import { reactive ,ref} from 'vue';

const add_dialog_visible=ref(false)
const addFormRef=ref()
const book_form=reactive({
    book_number:"",
    book_name:"",
    book_type:"",
    book_price:"",
    book_publisher:"",
    author:"",
    id:"",

})

const submitForm=(formEl)=>{
    // console.log(formEl)
    // console.log(book_form)
    axios.post(`http://localost:5000/book`,book_form).then(()=>{
        add_dialog_visible.value=false
        formEl.resetFields()
        getBooks()
    })
}
const resetForm=(formEl)=>{
    formEl.resetFields()
}
const handleClose=(done)=>{
    ElMessageBox.confirm('确认关闭？')
    .then(()=>{
        done();
    })
    .catch(()=>{
        console.log("数据保存出错")
    })
}
</script>

<template>
    <div>
        <h1 style="text-align: center;">图书管理系统</h1>
        <el-button type="primary" @click="add_dialog_visible = true" size="small">添加图书</el-button>
    <el-dialog title="添加图书" v-model="add_dialog_visible" width="30%" :before-close="handleClose">
        <el-form ref="addFormRef" :model="book_form" status-icon label-width="120px" class="demo-ruleForm">
            <el-form-item label="编号" prop="book_number">
                <el-input v-model="book_form.book_number" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="书名" prop="book_name">
                <el-input v-model="book_form.book_name" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="类型" prop="book_type">
                <el-input v-model="book_form.book_type" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="价格" prop="book_price">
                <el-input v-model="book_form.book_price" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="作者" prop="author">
                <el-input v-model="book_form.author" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="出版社" prop="book_publisher">
                <el-input v-model="book_form.book_publisher" autocomplete="off"/>
            </el-form-item>
            <el-form-item >
                <el-button type="primary" @click="submitForm(addFormRef)">提交</el-button>
                <el-button @click="resetForm(addFormRef)">重置</el-button>
            </el-form-item>


        </el-form>
    </el-dialog>
</div>
</template>

<style scoped></style>
