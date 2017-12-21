<template>
    <div class="table">
        <div class="crumbs">
            <el-breadcrumb separator="/">
                <el-breadcrumb-item><i class="el-icon-menu"></i> 表格</el-breadcrumb-item>
                <el-breadcrumb-item>Vue表格组件</el-breadcrumb-item>
            </el-breadcrumb>
        </div>
        <div class="plugins-tips">
            vue-datasource：一个用于动态创建表格的vue.js服务端组件。
            访问地址：<a href="https://github.com/coderdiaz/vue-datasource" target="_blank">vue-datasource</a>
        </div>
        <div class="form-box">
             <el-form ref="form" :model="form" label-width="80px">
                <el-form-item label="设备编号">
                    <el-select v-model="form.region" placeholder="请选择">
                        <el-option key="PK2400" label="PK2400" value="PK2400"></el-option>
                        <el-option key="PK2401" label="PK2401" value="PK2401"></el-option>
                        <el-option key="PK2402" label="PK2402" value="PK2402"></el-option>
                    </el-select>
                </el-form-item>
            </el-form>
        </div>
        <datasource language="en" :table-data="information.data" :columns="information.columns" :pagination="information.pagination"
                :actions="actions"
                v-on:change="changePage"
                v-on:searching="onSearch">
                </datasource>
    </div>
</template>

<script>
import { getinit, getcolumn } from "../../api/api";
import axios from "axios";
import Datasource from "vue-datasource";
export default {
  data: function() {
    const self = this;
    return {
      // url: "./static/datasource.json",
      information: {
        pagination: {},
        data: [{ id: "0", owner: "1" }],
        columns: [
          {
            name: "Id",
            key: "id"
          },
          {
            name: "Owner",
            key: "owner"
          }
        ]
      },
      form: {
        name: "",
        region: ""
      },
      actions: [
        {
          text: "Click",
          class: "btn-primary",
          event(e, row) {
            self.$message("选中的行数： " + row.row.id);
          }
        }
      ],
      query: ""
    };
  },
  components: {
    Datasource
  },
  methods: {
    changePage(values) {
      this.information.pagination.per_page = values.perpage;
      this.information.data = this.information.data;
    },
    onSearch(searchQuery) {
      this.query = searchQuery;
    },
    getResultByAxio() {
      getinit({
        params: {
          format: "json"
        }
      }).then(response => {
        console.log("response:", response.data);
        this.information.columns = response.data.columns;        
        this.information.data = response.data.results;
        console.log("this.information.data:", this.information);
      });
    }
  },
  created() {
    this.getResultByAxio();
  }
};
</script>

<style src="../../../static/css/datasource.css"></style>