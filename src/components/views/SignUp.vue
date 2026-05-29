<template>
  <div class="signup-container">
    <div class="signup-card">
      <h1>Create Account</h1>
      <form @submit.prevent="handleSignUp">
        <div class="form-group">
          <label for="fullname">Full Name</label>
          <input 
            v-model="formData.fullname" 
            type="text" 
            id="fullname" 
            placeholder="Enter your full name"
            required 
          />
        </div>

        <div class="form-group">
          <label for="email">Email Address</label>
          <input 
            v-model="formData.email" 
            type="email" 
            id="email" 
            placeholder="Enter your email"
            required 
          />
        </div>

        <div class="form-group">
          <label for="phone">Phone Number</label>
          <input 
            v-model="formData.phone" 
            type="tel" 
            id="phone" 
            placeholder="Enter your phone number"
            required 
          />
        </div>

        <div class="form-group">
          <label for="password">Password</label>
          <input 
            v-model="formData.password" 
            type="password" 
            id="password" 
            placeholder="Create a password"
            required 
          />
        </div>

        <div class="form-group">
          <label for="confirmpass">Confirm Password</label>
          <input 
            v-model="formData.confirmpass" 
            type="password" 
            id="confirmpass" 
            placeholder="Confirm your password"
            required 
          />
        </div>

        <div class="terms-check">
          <label>
            <input type="checkbox" required /> I agree to the Terms and Conditions
          </label>
        </div>

        <button type="submit" class="signup-btn">Sign Up</button>
      </form>

      <div class="login-link">
        Already have an account? <router-link to="/login">Login</router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const formData = ref({
  fullname: '',
  email: '',
  phone: '',
  password: '',
  confirmpass: ''
})

const handleSignUp = () => {
  if (formData.value.password !== formData.value.confirmpass) {
    alert('Passwords do not match!')
    return
  }
  console.log('Sign up attempt:', formData.value)
  alert('Account created successfully!')
  formData.value = { fullname: '', email: '', phone: '', password: '', confirmpass: '' }
}
</script>

<style scoped>
.signup-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: calc(100vh - 60px);
  background: linear-gradient(135deg, #ecfdf5 0%, #dbeafe 100%);
  padding: 20px;
}

.signup-card {
  background: rgba(255,255,255,0.96);
  padding: 40px;
  border-radius: 24px;
  box-shadow: 0 18px 40px rgba(6, 95, 70, 0.18);
  border: 1px solid #bbf7d0;
  width: 100%;
  max-width: 450px;
}

h1 {
  text-align: center;
  margin-bottom: 30px;
  color: #333;
}

.form-group {
  margin-bottom: 18px;
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
  border-color: #047857;
}

.terms-check {
  margin-bottom: 20px;
}

.terms-check label {
  display: flex;
  align-items: center;
  cursor: pointer;
  font-weight: normal;
}

.terms-check input {
  margin-right: 8px;
}

.signup-btn {
  width: 100%;
  padding: 12px;
  background: linear-gradient(135deg, #047857 0%, #15803d 100%);
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 1.1em;
  font-weight: 600;
  cursor: pointer;
  transition: transform 0.3s;
}

.signup-btn:hover {
  transform: translateY(-2px);
}

.login-link {
  text-align: center;
  margin-top: 20px;
  color: #666;
}

.login-link a {
  color: #047857;
  text-decoration: none;
  font-weight: 600;
  transition: color 0.3s;
}

.login-link a:hover {
  color: #166534;
}
</style>
