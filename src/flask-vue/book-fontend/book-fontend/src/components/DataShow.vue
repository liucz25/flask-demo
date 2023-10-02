<script setup>
import axios from 'axios';
import { ref, reactive, onMounted } from 'vue'
import { ElMessageBox } from 'element-plus';

const books = reactive([])
const getBooks = () => {
    axios.get("http://localhost:5000/books",).then(res => {
        books.splice(0, books.length)
        // console.log(res)
        books.push(...res.data.result)
        console.log("前端获得数据")
    })
}
onMounted(() => {
    getBooks()
})


const handelDelete = (index, scope) => {
    console.log(index, scope.id)
    axios.delete(`http://localhost:5000/books/${scope.id}`).then(() => {
        getBooks()
    })
}
const book_form = reactive({
    book_number: "",
    book_name: "",
    book_type: "",
    book_price: "",
    book_publisher: "",
    author: "",
    id: "",

})

const handleEdit = (index, scope) => {
    // console.log("*"*20,index,scope)
    for (let key in scope) {
        book_form[key] = scope[key]
    }
    // console.log(book_form)
    edit_dialog_visible.value = true
    // submitEditForm(book_form)
}

const edit_dialog_visible = ref(false)
const editFormRef = ref()



const submitEditForm = (formEl) => {
    // console.log(formEl)
    console.log(book_form.id, book_form)
    axios.put(`http://localhost:5000/books/${book_form.id}`, book_form).then(() => {
        console.log("ok")
        formEl.resetFields()
        edit_dialog_visible.value = false
        getBooks()
    })
}



const resetForm = (formEl) => {
    formEl.resetFields()
}
const handleClose = (done) => {
    ElMessageBox.confirm('确认关闭？')
        .then(() => {
            done();
        })
        .catch(() => {
            console.log("数据保存出错")
        })
}

</script>

<template>
    <div style="margin: 0 auto;">

        <el-table :data="books" style="margin: 20px auto;">
            <el-table-column label="编号" prop="book_number" />
            <el-table-column label="书名" prop="book_name" />
            <el-table-column label="类型" prop="book_type" />
            <el-table-column label="价格" prop="book_prize" />
            <el-table-column label="作者" prop="author" />
            <el-table-column label="出版社" prop="book_publisher" />
            <el-table-column align="right" label="操作" width="200px">
                <template #default="scope">
                    <!-- <template slot-scope='scope'> -->
                    <el-button size="small" @click="handleEdit(scope.$index, scope.row)">
                        编辑
                    </el-button>
                    <el-button size="small" @click="handelDelete(scope.$index, scope.row)">
                        删除
                    </el-button>
                </template>
            </el-table-column>
        </el-table>


        <div>

<el-dialog title="编辑图书" v-model="edit_dialog_visible" width="30%" :before-close="handleClose">
    <el-form ref="editFormRef" :model="book_form" status-icon label-width="120px" class="demo-ruleForm">
        <el-form-item label="编号" prop="book_number">
            <el-input v-model="book_form.book_number" autocomplete="off" />
        </el-form-item>
        <el-form-item label="书名" prop="book_name">
            <el-input v-model="book_form.book_name" autocomplete="off" />
        </el-form-item>
        <el-form-item label="类型" prop="book_type">
            <el-input v-model="book_form.book_type" autocomplete="off" />
        </el-form-item>
        <el-form-item label="价格" prop="book_price">
            <el-input v-model="book_form.book_price" autocomplete="off" />
        </el-form-item>
        <el-form-item label="作者" prop="author">
            <el-input v-model="book_form.author" autocomplete="off" />
        </el-form-item>
        <el-form-item label="出版社" prop="book_publisher">
            <el-input v-model="book_form.book_publisher" autocomplete="off" />
        </el-form-item>
        <el-form-item>
            <el-button type="primary" @click="submitEditForm(editFormRef)">提交</el-button>
            <el-button @click="resetForm(editFormRef)">重置</el-button>
        </el-form-item>


    </el-form>
</el-dialog>
</div>



    </div>
</template>

<style scoped></style>
