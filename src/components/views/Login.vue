<template>
  <div class="login-container">
    <div class="login-card">
      <h1>Login</h1>
      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label for="email">Email Address</label>
          <input 
            v-model="credentials.email" 
            type="email" 
            id="email" 
            placeholder="Enter your email"
            required 
          />
        </div>

        <div class="form-group">
          <label for="password">Password</label>
          <input 
            v-model="credentials.password" 
            type="password" 
            id="password" 
            placeholder="Enter your password"
            required 
          />
        </div>

        <div class="remember-forgot">
          <label class="remember">
            <input type="checkbox" /> Remember me
          </label>
          <a href="#" class="forgot-link">Forgot Password?</a>
        </div>

        <button type="submit" class="login-btn">Login</button>
      </form>

      <div class="divider">or</div>

      <div class="social-login">
        <button class="social-btn google">
          <span>🔵 Google</span>
        </button>
        <button class="social-btn facebook">
          <span>f Facebook</span>
        </button>
      </div>

      <div class="signup-link">
        Don't have an account? <router-link to="/signup">Sign Up</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const credentials = ref({
  email: '',
  password: ''
})

const handleLogin = () => {
  console.log('Login attempt:', credentials.value)
  alert('Login successful!')
  credentials.value = { email: '', password: '' }
}
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 60px);
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;
}

.login-card {
  background: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  width: 100%;
  max-width: 400px;
}

h1 {
  text-align: center;
  margin-bottom: 30px;
  color: #333;
}

.form-group {
  margin-bottom: 20px;
}

.form-group label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
  color: #333;
}

.form-group input {
  width: 100%;
  padding: 12px;
  border: 2px solid #ddd;
  border-radius: 5px;
  font-size: 1em;
  transition: border-color 0.3s;
}

.form-group input:focus {
  outline: none;
  border-color: #667eea;
}

.remember-forgot {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
  font-size: 0.9em;
}

.remember {
  display: flex;
  align-items: center;
  cursor: pointer;
}

.remember input {
  margin-right: 5px;
}

.forgot-link {
  color: #667eea;
  text-decoration: none;
  transition: color 0.3s;
}

.forgot-link:hover {
  color: #764ba2;
}

.login-btn {
  width: 100%;
  padding: 12px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1.1em;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.3s;
}

.login-btn:hover {
  transform: translateY(-2px);
}

.divider {
  text-align: center;
  margin: 20px 0;
  color: #999;
  position: relative;
}

.divider::before,
.divider::after {
  content: '';
  position: absolute;
  top: 50%;
  width: 45%;
  height: 1px;
  background: #ddd;
}

.divider::before {
  left: 0;
}

.divider::after {
  right: 0;
}

.social-login {
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}

.social-btn {
  flex: 1;
  padding: 10px;
  border: 2px solid #ddd;
  background: white;
  border-radius: 5px;
  cursor: pointer;
  transition: all 0.3s;
}

.social-btn:hover {
  border-color: #667eea;
}

.social-btn.google:hover {
  background: #f0f0f0;
}

.social-btn.facebook:hover {
  background: #f0f0f0;
}

.signup-link {
  text-align: center;
  color: #666;
}

.signup-link a {
  color: #667eea;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s;
}

.signup-link a:hover {
  color: #764ba2;
}
</style>
